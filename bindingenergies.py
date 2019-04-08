import os
import re
import pandas as pd
import numpy as np
import shutil
import subprocess
import multiprocessing

with open(os.path.join('base', 'input.py')) as infile:
    input_file = infile.read()
    
base_directory = 'binding_energies'
def directory(carbon,nitrogen):
    return os.path.join(base_directory, "c{:.3f}n{:.3f}".format(carbon,nitrogen))

def make_input(binding_energies):
    """
    Make an input file for the given (carbon,oxygen) tuple (or iterable) of binding energies
    and return the name of the directory in which it is saved.
    """
    carbon, nitrogen = binding_energies
    output = input_file
    out_dir = directory(carbon, nitrogen)
    carbon_string = "'C':({:f}, 'eV/molecule')".format(carbon)
    output = re.sub("'C':\(.*?, 'eV/molecule'\)", carbon_string, output)
    nitrogen_string = "'N':({:f}, 'eV/molecule')".format(nitrogen)
    output = re.sub("'N':\(.*?, 'eV/molecule'\)", nitrogen_string, output)
    os.path.exists(out_dir) or os.makedirs(out_dir)
    out_file = os.path.join(out_dir, 'input.py')
    with open(out_file,'w') as outfile:
        outfile.write(output)
    shutil.copy(os.path.join('base','run.sh'), out_dir)
    return out_dir

carbon_range = (-7.5, -2)
nitrogen_range = (-6.5, -1.5)
grid_size = 9
mesh  = np.mgrid[carbon_range[0]:carbon_range[1]:grid_size*1j, nitrogen_range[0]:nitrogen_range[1]:grid_size*1j]

experiments = mesh.reshape((2,-1)).T

map(make_input, experiments)
