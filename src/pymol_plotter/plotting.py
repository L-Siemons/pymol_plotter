
import pandas as pd

from importlib import resources
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

class PymolPlotter():
    """
        A utility to generate PyMOL (.pml) scripts for property mapping.

        This class reads data from a CSV, normalizes values to a colormap, 
        and generates PyMOL selection and coloring commands. It is designed 
        to automate the visualization of residue-level or atom-level data 
        onto 3D structures.

        Attributes:
            df (pd.DataFrame): The data loaded from the CSV file.
            lower_color_scale (float): The minimum value for color normalization (A).
            upper_color_scale (float): The maximum value for color normalization (B).
            colormap (str): The Matplotlib colormap name used for plotting.
            save_file (str): The filename where the .pml script will be saved.
            pdb_file (str): Path to the structure file to be loaded in PyMOL.
            text (str): The generated PyMOL command string.
            show_spheres (bool) : show spheres for the selection
        """
    
    def __init__(self,
                 pdb_file,
                 csv, 
                 lower_color_scale, 
                 upper_color_scale, 
                 colormap='viridis', 
                 base_file='default', 
                 save_file='value_out.pml', 
                 show_spheres=False):
        """
        Initializes the plotter and triggers the text building process.

        Args:
            pdb_file (str): Path to the PDB file.
            csv (str): Path to the CSV containing 'value' and selection columns.
            lower_color_scale (float): Value mapped to the bottom of the colormap.
            upper_color_scale (float): Value mapped to the top of the colormap.
            colormap (str, optional): Matplotlib colormap name. Defaults to 'viridis'.
            base_file (str, optional): Template setting. Defaults to 'default'.
            save_file (str, optional): Target .pml filename. Defaults to 'value_out.pml'.
            show_spheres (bool, optional) : show spheres for the selection, not shown by default

        Raises:
            NotImplementedError: If a non-default base_file is specified.
        """

        self.df = pd.read_csv(csv)
        self.csv = csv
        self.lower_color_scale = lower_color_scale
        self.upper_color_scale = upper_color_scale
        self.colormap = colormap
        self.save_file = save_file
        self.pdb_file = pdb_file
        self.show_spheres = show_spheres

        if base_file == 'default':
            self.template_filename = 'base.pml'
            self.template = self._load_template()
            self.base_message = self._build_default_base_message()
        else:
            raise NotImplementedError('This option for base_file needs to be implimented')
        
        self._build_text()
        
    
    def _load_template(self) -> str:
        """
        Loads the base .pml template from the package resources.

        Returns:
            str: The raw text content of the template file.
        """
        template_path = resources.files(__package__).joinpath('dat', self.template_filename)

        with template_path.open("r", encoding="utf-8") as f:
            return f.read()

    def _build_default_base_message(self, ):
        """
        Populates the base template with specific file metadata.

        Returns:
            str: The formatted header for the PyMOL script.
        """

        kwargs = {
            'pdb_file' : self.pdb_file
        }

        return self.template.format(**kwargs) + '\n'

    def _build_text(self,):
        """
        Constructs the core PyMOL commands by iterating over the DataFrame.

        For each row, it creates a selection string based on all columns 
        except 'value', then maps the 'value' to a 0xRRGGBB hex code.

        Note:
            The selection is built using 'and' logic across all available 
            columns (e.g., 'resi 10 and chain A').
        """

        lines = [self.base_message]
        cmap = plt.get_cmap(self.colormap)
        norm = mcolors.Normalize(vmin=self.lower_color_scale, vmax=self.upper_color_scale)

        for index, row in self.df.iterrows():
            # create the selection
            line = 'sele '
            selection = []
            for col_title in self.df.columns:
                if col_title != 'value':
                    entry = row[col_title]
                    sele =  f' {col_title} {entry} '
                    selection.append(sele)
            
            # full line
            line += ' and '.join(selection)

            # to add the value
            value = entry = row['value']
            
            # create the colors
            rgb_floats = cmap(norm(value))[:3]
            hex_code = mcolors.to_hex(rgb_floats).lstrip('#')
            line += '\n'  + f'color 0x{hex_code}, sele'
            print(line)
            if self.show_spheres:
                line += ' \n show spheres, sele '
            lines.append(line)
        
        self.text = '\n'.join(lines)
    
    def save(self,):
        """
        Writes the generated command text to the specified save_file.

        Checks for the existence of the 'text' attribute before attempting 
        to write to disk.
        """

        if hasattr(self, "text"):
            out = open(self.save_file, 'w')
            out.write(self.text)
            out.close()
        else:
            print('[PymolPlotter] WARNING: self.text has not been written')



