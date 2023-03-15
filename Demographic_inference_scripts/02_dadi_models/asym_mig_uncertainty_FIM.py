import sys
import os
import numpy
import dadi
import Models_2D

# Import data to create joint-site frequency spectrum
snps = "/01_dadi_input/dadi_2pops_Mbalmayo_Ako_snps.txt"

#Create python dictionary from snps file
dd = dadi.Misc.make_data_dict(snps)

#pop_ids is a list which should match the populations headers of your SNPs file columns
pop_ids=["Mbalmayo", "Ako"]

#projection sizes, in ALLELES not individuals
proj = [24, 24]

#Convert this dictionary into folded AFS object
#[polarized = False] creates folded spectrum object
fs = dadi.Spectrum.from_data_dict(dd, pop_ids=pop_ids, projections = proj, polarized = False)

#print some useful information about the afs or jsfs
print("\n\n============================================================================")
print("\nData for site frequency spectrum:\n")
print("Projection: {}".format(proj))
print("Sample sizes: {}".format(fs.sample_sizes))
print("Sum of SFS: {}".format(numpy.around(fs.S(), 2)))
print("\n============================================================================\n")

#make sure to define your extrapolation grid size (based on your projections)
pts = [40,50,60]

#Provide best optimized parameter set for empirical data.
#These will come from previous analyses you have already completed.
emp_params = [1.2924,2.3196,11.0347,0.8229,0.7607]

#Indicate whether your frequency spectrum object is folded (True) or unfolded (False)
fs_folded = True

func = Models_2D.asym_mig
#create an extrapolating function
func_exec = dadi.Numerics.make_extrap_log_func(func)

#estimate uncertainties with FIM if you think your data is truly unlinked
uncerts_fim = dadi.Godambe.FIM_uncert(func_exec, pts, emp_params, fs, multinom=True, eps=0.01)
print('Estimated parameter standard deviations from FIM: {0}'.format(uncerts_fim))

filename = open("fim_uncertainty.txt", 'a')
filename.write('Estimated parameter standard deviations from FIM: {0}'.format(uncerts_fim))
filename.close()

