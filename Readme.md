# PymolPlotter

`PymolPlotter` is a Python utility designed to automate the process of mapping numerical data onto 3D structures in PyMOL. 

## Ussage

To use pymol plotter you need to construct a csv file that contains the values you would like to color according to under a coloumn named 'value' and the remaining coloumns should be used to specify the selection logic in pymol. 

For example the following csv:
```
resid,chain,name,value
1,A,c1',0.5209897
2,A,c1',0.57516559
```
will give rise to these lines in the pml file that pymol reads 
```
sele  resid 1  and  chain A  and  name c1'
color 0xfff5f0, sele
sele  resid 2  and  chain A  and  name c1'
color 0xfff5f0, sele
```

In `examples/` there is an example that plots the order parameters on the structure of the DNA helix. These values are taken from:  
```
How flexible is a DNA duplex ? An investigation by NMR relaxometry and molecular dynamics simulations
https://doi.org/10.26434/chemrxiv-2026-wzcx6
```

To run the example:
```
bash run.sh 
```
This should open a pymol session with the structure colored as below

![image info](example/dna.png)

To see how to configure the PymolPlotter please see the doc strings for `src/pymol_plotter/plotting/.py`.

## Installation
1) Make sure you have python3.14 or later. If not you can install this with Homebrew

2) If desired make a python virtual enviroment 
```
python3.14 -m venv pymol_plotter
source pymol_plotter/bin/activate
```

3) Install with pip:
```
$ pip install . 
```

## Authors 
Lucas Siemons

## If you would like to contribute - get in touch! 