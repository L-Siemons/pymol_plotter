load 5uzd.cif
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


sele  resid 1  and  chain A  and  name c1' 
color 0xfff5f0, sele 
 show spheres, sele 
sele  resid 2  and  chain A  and  name c1' 
color 0xfff5f0, sele 
 show spheres, sele 
sele  resid 3  and  chain A  and  name c1' 
color 0xfb7c5c, sele 
 show spheres, sele 
sele  resid 4  and  chain A  and  name c1' 
color 0xfc9070, sele 
 show spheres, sele 
sele  resid 5  and  chain A  and  name c1' 
color 0xfff5f0, sele 
 show spheres, sele 
sele  resid 6  and  chain A  and  name c1' 
color 0x67000d, sele 
 show spheres, sele 
sele  resid 7  and  chain A  and  name c1' 
color 0x860811, sele 
 show spheres, sele 
sele  resid 8  and  chain A  and  name c1' 
color 0xbe151a, sele 
 show spheres, sele 
sele  resid 9  and  chain A  and  name c1' 
color 0xfca98c, sele 
 show spheres, sele 
sele  resid 10  and  chain A  and  name c1' 
color 0xf4503a, sele 
 show spheres, sele 
sele  resid 11  and  chain A  and  name c1' 
color 0xfc9777, sele 
 show spheres, sele 
sele  resid 12  and  chain A  and  name c1' 
color 0xffeee7, sele 
 show spheres, sele 
sele  resid 14  and  chain B  and  name c1' 
color 0xfff5f0, sele 
 show spheres, sele 
sele  resid 15  and  chain B  and  name c1' 
color 0xfff5f0, sele 
 show spheres, sele 
sele  resid 16  and  chain B  and  name c1' 
color 0x67000d, sele 
 show spheres, sele 
sele  resid 17  and  chain B  and  name c1' 
color 0xc5171c, sele 
 show spheres, sele 
sele  resid 18  and  chain B  and  name c1' 
color 0xe93529, sele 
 show spheres, sele 
sele  resid 19  and  chain B  and  name c1' 
color 0xfff5f0, sele 
 show spheres, sele 
sele  resid 20  and  chain B  and  name c1' 
color 0xf5523a, sele 
 show spheres, sele 
sele  resid 22  and  chain B  and  name c1' 
color 0xfc8161, sele 
 show spheres, sele 
sele  resid 23  and  chain B  and  name c1' 
color 0xfcb095, sele 
 show spheres, sele 
sele  resid 24  and  chain B  and  name c1' 
color 0xfee8de, sele 
 show spheres, sele 