import sys
import os
import numpy
import dadi
import pylab
from datetime import datetime
import Optimize_Functions
import Models_2D


#===========================================================================
# Import data to create joint-site frequency spectrum
#===========================================================================

#**************
snps = "/01_dadi_input/dadi_2pops_Mbalmayo_Ako_snps.txt"

#Create python dictionary from snps file
dd = dadi.Misc.make_data_dict(snps)

#**************
#pop_ids is a list which should match the populations headers of your SNPs file columns
pop_ids=["Mbalmayo", "Ako"]

#**************
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

#create a prefix based on the population names to label the output files
#ex. Pop1_Pop2
prefix = "_".join(pop_ids)

#**************
#make sure to define your extrapolation grid size (based on your projections)
pts = [40,50,60]

#**************
#Set the number of rounds here
rounds = 5

#define the lists for optional arguments
#you can change these to alter the settings of the optimization routine

reps = [50,50,50,50,50]
maxiters = [10,15,15,15,20]
folds = [3,3,3,2,1]
#**************
#Indicate whether your frequency spectrum object is folded (True) or unfolded (False)
fs_folded = True

upper = [10,10,20,20,10]
lower = [0.01,0.01,0.01,0.01,0.1]


# Split into two populations, with continuous asymmetric migration.
Optimize_Functions.Optimize_Routine(fs, pts, prefix, "asym_mig", Models_2D.asym_mig, rounds, 5, fs_folded=fs_folded, in_upper = upper, in_lower = lower,
                                        reps=reps, maxiters=maxiters, folds=folds, param_labels = "nu1, nu2, m12, m21, T")
