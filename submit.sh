#!/bin/bash
#SBATCH --job-name=wikiparser
#SBATCH --output=${FILES[$SLURM_ARRAY_TASK_ID]}.out
#SBATCH --error=%A_%a.err
#SBATCH --ntasks=1
#SBATCH --nodes=1
#SBATCH --cpus-per-task=1
#SBATCH --time=5:00:00
#SBATCH --mem=4000

# load python and packages
module add python
export PYTHONPATH=/nas/longleaf/home/bill10/Library/lib/python3/:$PYTHONPATH

# grab out filename from the array
mapfile -t FILES < $1
FILENAME=${FILES[$SLURM_ARRAY_TASK_ID]}

# Copy files from Stash
#wget http://stash.osgconnect.net/+bill10/Wiki/$FILENAME
#7z e $FILENAME

# Run python script
python3 main.py $FILENAME $2 $3
