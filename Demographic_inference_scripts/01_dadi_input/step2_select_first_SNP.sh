#!/bin/bash

#slurm options
#SBATCH -p intel-sc3,amd-ep2
#SBATCH -q normal
#SBATCH -J first_SNP
#SBATCH -c 1
#SBATCH -o first_SNP.%j.log
#SBATCH --mem 4G

## user's own commands below

perl first_snp_vcfMiller.pl butterfly_denovo_38.recode.vcf butterfly_denovo_38_first_SNP.vcf

echo "** select first SNP done **"
