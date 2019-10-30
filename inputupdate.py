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
os.path.exists(base_directory) or os.makedirs(base_directory)

def directory(carbon,hydrogen):
    return os.path.join(base_directory, "c{:.3f}h{:.3f}".format(carbon,hydrogen))

def make_input(binding_energies):
    """
    Make an input file for the given (carbon,oxygen) tuple (or iterable) of binding energies
    and return the name of the directory in which it is saved.
    """
    carbon, hydrogen = binding_energies
    output = input_file
    out_dir = directory(carbon, hydrogen)
    carbon_string = "'C':({:f}, 'eV/molecule')".format(carbon)
    output = re.sub("'C':\(.*?, 'eV/molecule'\)", carbon_string, output)
    hydrogen_string = "'H':({:f}, 'eV/molecule')".format(hydrogen)
    output = re.sub("'H':\(.*?, 'eV/molecule'\)", hydrogen_string, output)
    os.path.exists(out_dir) or os.makedirs(out_dir)
    out_file = os.path.join(out_dir, 'input.py')
    with open(out_file,'w') as outfile:
        outfile.write(output)
    shutil.copy(os.path.join('base','run.sh'), out_dir)
    return out_dir

carbon_range = (-10.0, -2)
hydrogen_range = (-3.5, -1.5)
grid_size = 9
mesh  = np.mgrid[carbon_range[0]:carbon_range[1]:grid_size*1j, hydrogen_range[0]:hydrogen_range[1]:grid_size*1j]

experiments = mesh.reshape((2,-1)).T

map(make_input, experiments)
