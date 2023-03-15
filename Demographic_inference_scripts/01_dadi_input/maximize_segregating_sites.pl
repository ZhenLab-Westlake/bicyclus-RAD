#!/usr/bin/perl -w
use strict;

use List::Util qw(max);
my $file = shift;
open IN,"$file" or die $!;

my $output = shift;
open OUT,">$output" or die $!;

my @array;
while(<IN>){
	chomp;
	next if /^\s*($|sample)/;
	my @info = split;
	push @array,$info[2];
}
my $max_num = max @array;
print OUT "$max_num\n";
