#!/bin/bash

#slurm options
#SBATCH -p intel-sc3,amd-ep2
#SBATCH -q normal
#SBATCH -J depth_vcftools
#SBATCH -c 1
#SBATCH -o depth_vcftools.%j.log

## user's own commands below

module load vcftools/0.1.16
vcftools --gzvcf butterfly_denovo_156_99_80_snps.dat2.vcf.gz --depth --out depth_vcftools.txt

echo "** stat depth done **"
