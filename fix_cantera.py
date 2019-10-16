#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Adapted from https://github.com/comocheng/rmgcat-pt-supporting-info/blob/master/RMG_CH4catcombust_Pt_nogas/fix_cantera.py

The version of ck2cti in the version of ck2cti in the version of Cantera
that is currently  in use by the authors has a bug that won't translate any reactions
from the surface file if there are no reactions in the gas phase
file. The work-around is to add a dummy gas phase reaction,
then run the translation, and then remove the dummy reaction.
"""

import os
import cantera as ct
from cantera import ck2cti
import sys

# load the paths of the binding energies
array = os.listdir('./binding_energies/')
lsrs = ['./binding_energies/' + x for x in array]

# add the base to the loop
lsrs.append('./base')

for x in lsrs:
    # first load the gas chemkin file to see if there are any gas reactions
    try:
        gas = ct.Solution(x + '/cantera/chem_annotated.cti', 'gas')
    except:
        print("There is no {}/cantera/chem_anotated.cti".format(x))
        continue

    if gas.n_reactions == 0:
        print("Fixing for {}".format(x))

        # add in the placeholder reaction
        original_chemkin = str(x) + '/chemkin/chem_annotated-gas.inp'
        temporary_chemkin = str(x) + '/chemkin/chem_annotated-gas-fixed.inp'
        temporary_cantera = str(x) + '/cantera/chem_annotated-fixed.cti'
        final_cantera = str(x) + '/cantera/chem_annotated.cti'
        surface_file_location = str(x) + '/chemkin/chem_annotated-surface.inp'

        # Reading chemkin file
        with open(original_chemkin, 'r') as f:
            t = f.read()

        # Adding dummy reaction
        t = t.replace('REACTIONS    KCAL/MOLE   MOLES\n\nEND',
        'REACTIONS    KCAL/MOLE   MOLES\nN2 <=> N2 0 0 0\nEND')

        # Saving modified chemkin file
        with open(temporary_chemkin,'w') as f:
            f.write(t)

        # Translating to cantera file
        parser = ck2cti.Parser()
        surfaces = parser.convertMech(inputFile=temporary_chemkin,
                                      thermoFile=None,
                                      transportFile=None,
                                      surfaceFile=surface_file_location,
                                      phaseName='gas',
                                      outName=temporary_cantera,
                                      permissive=True)

        # Reading cantera file
        with open(temporary_cantera) as f:
            t = f.read()

        # Removing dummy reaction
        t = t.replace('\# Reaction 1\nreaction(\'N2 <=> N2\', [0.000000e+00, 0.0, 0.0],\n         id=\'gas-1\')','\n')

        # Saving cantera file
        with open(final_cantera,'w') as f:
            f.write(t)

        # Deleting temporary chemkin file
        os.remove(temporary_chemkin)
        # Deleting temporary cantera file
        os.remove(temporary_cantera)
    else:
        continue
