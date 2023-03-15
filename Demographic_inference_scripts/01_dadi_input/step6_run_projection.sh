#!/bin/bash

#slurm options
#SBATCH -p intel-sc3,amd-ep2
#SBATCH -q normal
#SBATCH -J projection
#SBATCH -c 1
#SBATCH -o projection.%j.log
#SBATCH --mem 4G

module load  anaconda3
conda activate dadi

python dadi_2D_projection.py

echo "** projection done **"


