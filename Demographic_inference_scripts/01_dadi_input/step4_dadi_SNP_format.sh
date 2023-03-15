#!/bin/bash

#slurm options
#SBATCH -p intel-sc3,amd-ep2
#SBATCH -q normal
#SBATCH -J dadi_input
#SBATCH -c 1
#SBATCH -o dadi_input.%j.log
#SBATCH --mem 4G

module load  anaconda3
conda activate dadi

python hap_to_dadiSNP.py ./butterfly_denovo_38_first_SNP_haplotype.tsv /01_dadi_input
