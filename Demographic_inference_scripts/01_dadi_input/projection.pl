#!/usr/bin/perl -w
use strict;

my $snp_file = shift;
my $pop1 = shift;
my $pop2 = shift;

my $num1 = shift;
my $num2 = shift;

my $output = shift;
open OUT,">$output" or die $!;

print OUT "import dadi\n";
print OUT "'''\nusage: python dadi_2D_projections.py\nFind the best combination of downsampling for maximizing number of segregating sites.\n'''\n";

print OUT "\#get snps file\n";
print OUT "snps1 = \"$snp_file\"\n\n";

print OUT "\#Create python dictionary from snps file\n";
print OUT "dd1 = dadi.Misc.make_data_dict(snps1)\n";
print OUT "\#pop_ids is a list which should match the populations headers of your SNPs file columns\n";
print OUT "pop_ids=[\"$pop1\", \"$pop2\"]\n";

print OUT "\#projection sizes, in ALLELES not individuals\n";
for(my $i=2;$i<=$num1;$i+=2){
        for(my $j=2;$j<=$num2;$j+=2){
                print OUT "proj_1 = [$i,$j]\n";
		print OUT "fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)\n";
		print OUT "print (\"sample sizes {}\".format(fs_1.sample_sizes))\nprint (\"Segregating sites {}\".format(fs_1.S()))\n";
        }
}
close OUT;
