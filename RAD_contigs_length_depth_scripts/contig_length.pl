#!/usr/bin/perl -w
use strict;
use POSIX;

my $fasta = shift;
my $out = shift;

open IN, "$fasta" or die $!;

open OUT,">$out" or die $!;
print OUT "loci\tlength\n";

my %hash;
my $sequence = "";

my $geneid;

while(<IN>){
	chomp;
	my $line = $_;
	if ($line =~ /^>(\S+)/){
		$geneid = $1;
		$sequence = "";
	}else{
		$sequence = $sequence.$line;
		$hash{$geneid}=length($sequence);
	}
}

foreach my $loci (sort keys %hash){
	print OUT "$loci\t$hash{$loci}\n";
}

close IN;
close OUT;
