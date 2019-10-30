#!/bin/bash
#SBATCH --job-name=eRMGcat
#SBATCH --error=error.log
#SBATCH --output=output.log
#SBATCH -n1
#SBATCH --partition=west,general,fullnode
#SBATCH --exclude=c5003
#SBATCH --mem=250Gb
#SBATCH --time=24:00:00

echo $RMGpy
python  $RMGpy/rmg.py -p -t 00:23:59:59 input.py
