#!/bin/bash

#slurm options
#SBATCH -p intel-sc3,amd-ep2
#SBATCH -q normal
#SBATCH -J vcf2hap
#SBATCH -c 1
#SBATCH -o vcf2hap.%j.log
#SBATCH --mem 4G

perl vcf2haplotype.pl butterfly_denovo_38_first_SNP.vcf.gz butterfly_denovo_38_first_SNP_haplotype.tsv

echo "** convert vcf to hap done **"
