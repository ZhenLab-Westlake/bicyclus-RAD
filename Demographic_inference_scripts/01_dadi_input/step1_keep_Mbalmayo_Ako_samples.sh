#!/bin/bash

#slurm options
#SBATCH -p intel-sc3,amd-ep2
#SBATCH -q normal
#SBATCH -J filter
#SBATCH -c 1
#SBATCH -o filter.%j.log
#SBATCH --mem 4G

## user's own commands below

module load vcftools/0.1.16

vcftools --gzvcf ./butterfly_denovo_156_99_80_snps.dat2.vcf.gz --mac 1 --min-alleles 2 --max-alleles 2 --keep 38_samples_Mbalmayo_Ako --recode --out butterfly_denovo_38

echo "** filter vcf done **"
