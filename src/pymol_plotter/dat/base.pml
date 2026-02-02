load {pdb_file}
hide all
show cartoon
set cartoon_side_chain_helper, on

set specular, 0
set ray_shadow, off
set antialias, 2
set ray_trace_mode, 1
set ray_trace_disco_factor, 1
set ray_trace_gain, 0.1
set ambient, 0.4
set direct, 0.45
set cartoon_sampling, 10
set ray_trace_color, black
set reflect, 1
set reflect_power, 0

# Structure preferences
set ribbon_width, 8
set line_width, 2.5
set cartoon_transparency, 0.35
set stick_transparency, 0.35
set cartoon_flat_sheets, off
set valence, off
set dash_length, 0.06
set dash_radius, 0.12
set cartoon_gap_cutoff, 0

#and better colors:
set_color nitrogen = [2, 118, 253]

set_color good_red, [228,74,62]
set_color good_yellow, [250,199,44]
set_color good_teal, [40,176,193]
set_color good_green, [170,195,47]
set_color good_pink, [236,114,164]
set_color good_peach, [249,145,120]
set_color good_blue, [68,153,231]
set cartoon_nucleic_acid_mode, 1

color good_teal, all
