#!perl -w
#perl first_snp_vcf.pl vcffile output-vcffile
#given a vcf file of radtag snps, output the first snps of each radtag

$vcf = shift (@ARGV); chomp $vcf;
open IN, $vcf or die "cannot open vcf file";
$out = shift (@ARGV); chomp $out;
open OUT, ">$out";

@taglist =();
while ($line = <IN> ){
	chomp $line;
	if ($line =~ m/^#/){
		print OUT $line, "\n";
	}
	else {
		($chr, $pos, $id) = split('\t', $line);
		if ($chr ~~ @taglist){}
		else {
			print OUT $line, "\n";
			push @taglist, $chr;
		} 
	}
}

