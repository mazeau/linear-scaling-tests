#!/bin/bash
#SBATCH --job-name=RMGcat
#SBATCH --error=error.log
#SBATCH --output=output.log
#SBATCH --cpus-per-task=4
#SBATCH --ntasks=1
#SBATCH --partition=west,short,large,gpu
#SBATCH --exclude=c5003
#SBATCH --mem=50Gb
#SBATCH --time=6:00:00

echo $RMGpy
source activate rmg_env
python  $RMGpy/rmg.py -p input.py
