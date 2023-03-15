import dadi
'''
usage: python dadi_2D_projections.py
Find the best combination of downsampling for maximizing number of segregating sites.
'''
#get snps file
snps1 = "/01.dadi_input/dadi_2pops_Mbalmayo_Ako_snps.txt"

#Create python dictionary from snps file
dd1 = dadi.Misc.make_data_dict(snps1)
#pop_ids is a list which should match the populations headers of your SNPs file columns
pop_ids=["Mbalmayo", "Ako"]
#projection sizes, in ALLELES not individuals
proj_1 = [2,2]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [2,4]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [2,6]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [2,8]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [2,10]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [2,12]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [2,14]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [2,16]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [2,18]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [2,20]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [2,22]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [2,24]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [2,26]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [2,28]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [2,30]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [2,32]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [4,2]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [4,4]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [4,6]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [4,8]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [4,10]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [4,12]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [4,14]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [4,16]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [4,18]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [4,20]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [4,22]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [4,24]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [4,26]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [4,28]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [4,30]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [4,32]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [6,2]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [6,4]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [6,6]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [6,8]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [6,10]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [6,12]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [6,14]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [6,16]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [6,18]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [6,20]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [6,22]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [6,24]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [6,26]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [6,28]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [6,30]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [6,32]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [8,2]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [8,4]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [8,6]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [8,8]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [8,10]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [8,12]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [8,14]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [8,16]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [8,18]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [8,20]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [8,22]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [8,24]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [8,26]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [8,28]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [8,30]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [8,32]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [10,2]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [10,4]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [10,6]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [10,8]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [10,10]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [10,12]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [10,14]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [10,16]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [10,18]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [10,20]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [10,22]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [10,24]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [10,26]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [10,28]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [10,30]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [10,32]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [12,2]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [12,4]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [12,6]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [12,8]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [12,10]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [12,12]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [12,14]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [12,16]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [12,18]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [12,20]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [12,22]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [12,24]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [12,26]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [12,28]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [12,30]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [12,32]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [14,2]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [14,4]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [14,6]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [14,8]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [14,10]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [14,12]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [14,14]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [14,16]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [14,18]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [14,20]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [14,22]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [14,24]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [14,26]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [14,28]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [14,30]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [14,32]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [16,2]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [16,4]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [16,6]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [16,8]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [16,10]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [16,12]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [16,14]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [16,16]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [16,18]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [16,20]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [16,22]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [16,24]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [16,26]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [16,28]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [16,30]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [16,32]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [18,2]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [18,4]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [18,6]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [18,8]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [18,10]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [18,12]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [18,14]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [18,16]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [18,18]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [18,20]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [18,22]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [18,24]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [18,26]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [18,28]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [18,30]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [18,32]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [20,2]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [20,4]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [20,6]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [20,8]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [20,10]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [20,12]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [20,14]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [20,16]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [20,18]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [20,20]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [20,22]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [20,24]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [20,26]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [20,28]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [20,30]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [20,32]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [22,2]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [22,4]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [22,6]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [22,8]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [22,10]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [22,12]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [22,14]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [22,16]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [22,18]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [22,20]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [22,22]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [22,24]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [22,26]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [22,28]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [22,30]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [22,32]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [24,2]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [24,4]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [24,6]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [24,8]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [24,10]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [24,12]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [24,14]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [24,16]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [24,18]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [24,20]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [24,22]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [24,24]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [24,26]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [24,28]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [24,30]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [24,32]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [26,2]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [26,4]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [26,6]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [26,8]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [26,10]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [26,12]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [26,14]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [26,16]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [26,18]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [26,20]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [26,22]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [26,24]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [26,26]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [26,28]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [26,30]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [26,32]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [28,2]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [28,4]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [28,6]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [28,8]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [28,10]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [28,12]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [28,14]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [28,16]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [28,18]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [28,20]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [28,22]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [28,24]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [28,26]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [28,28]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [28,30]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [28,32]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [30,2]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [30,4]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [30,6]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [30,8]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [30,10]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [30,12]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [30,14]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [30,16]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [30,18]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [30,20]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [30,22]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [30,24]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [30,26]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [30,28]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [30,30]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [30,32]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [32,2]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [32,4]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [32,6]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [32,8]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [32,10]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [32,12]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [32,14]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [32,16]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [32,18]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [32,20]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [32,22]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [32,24]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [32,26]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [32,28]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [32,30]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [32,32]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [34,2]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [34,4]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [34,6]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [34,8]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [34,10]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [34,12]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [34,14]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [34,16]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [34,18]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [34,20]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [34,22]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [34,24]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [34,26]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [34,28]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [34,30]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [34,32]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [36,2]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [36,4]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [36,6]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [36,8]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [36,10]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [36,12]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [36,14]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [36,16]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [36,18]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [36,20]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [36,22]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [36,24]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [36,26]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [36,28]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [36,30]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [36,32]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [38,2]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [38,4]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [38,6]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [38,8]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [38,10]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [38,12]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [38,14]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [38,16]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [38,18]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [38,20]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [38,22]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [38,24]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [38,26]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [38,28]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [38,30]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [38,32]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [40,2]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [40,4]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [40,6]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [40,8]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [40,10]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [40,12]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [40,14]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [40,16]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [40,18]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [40,20]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [40,22]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [40,24]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [40,26]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [40,28]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [40,30]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [40,32]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [42,2]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [42,4]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [42,6]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [42,8]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [42,10]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [42,12]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [42,14]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [42,16]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [42,18]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [42,20]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [42,22]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [42,24]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [42,26]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [42,28]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [42,30]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [42,32]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [44,2]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [44,4]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [44,6]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [44,8]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [44,10]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [44,12]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [44,14]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [44,16]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [44,18]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [44,20]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [44,22]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [44,24]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [44,26]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [44,28]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [44,30]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
proj_1 = [44,32]
fs_1 = dadi.Spectrum.from_data_dict(dd1, pop_ids=pop_ids, projections = proj_1, polarized = False)
print ("sample sizes {}".format(fs_1.sample_sizes))
print ("Segregating sites {}".format(fs_1.S()))
