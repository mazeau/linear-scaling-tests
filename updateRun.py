### update run.sh from base
import os
import shutil

array = os.listdir('./binding_energies')
files = ['./binding_energies/' + x for x in array]

for x in files:
    shutil.copy('./base/run.sh', x)

