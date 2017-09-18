#!/bin/bash
# This file will read in a file containing all wiki dump names, and submit the batch file
# Input: a text file, one dump per line.

mapfile -t FILES < $1

# get size of array
N=${#FILES[@]}
# now subtract 1 as we have to use zero-based indexing (first cell is 0)
N1=$(($N - 1))


# now submit to SLURM
if [ $N1 -ge 0 ]; then
    sbatch --array=0-$N1 submit.sh
fi
