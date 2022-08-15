#!/usr/bin/env python

import sys, os
from ase.io import write
from ase.io import read
from ase.io import espresso
from ase.visualize import view
#from ase.lattice.surface import surface

outfile = 'POSCAR'
# Next, run a simple conditonal statement to check if argv exists
if len(sys.argv) > 1:
    result = sys.argv[1]
else:
    result = False
    print("\n PROVIDE 'pdb' FILE IN THE SAME LINE.. [python pdb_to_poscar.py sample.pdb POSCAR]\n")
    exit()

#Reading PDB filename as an argument from the same line
infile = sys.argv[1]

#pdbformat=read('1.pdb',0,format='proteindatabank')
pdbformat = read(infile, 0, format='proteindatabank')
write(outfile, pdbformat, format='vasp')
print('outfile written in', outfile, 'format')
