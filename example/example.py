import pymol_plotter as pp

Plotter = pp.PymolPlotter('5uzd.cif', 's2.csv',0.6,0.8, show_spheres=True, colormap='Reds')
Plotter.save()
