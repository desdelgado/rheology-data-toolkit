import h5py



f = h5py.File("mytestfile.hdf5", "w")

dset = f.create_dataset("mydataset", (100,), dtype='i')

f = h5py.File('mydataset.hdf5', 'a')

grp = f.create_group("subgroup")

dset2 = grp.create_dataset("another_dataset", (50,), dtype='f')

dset2 = grp.create_dataset("another_one_dataset", (50,), dtype='f')
dset3 = f.create_dataset('subgroup2/dataset_three', (10,), dtype='i')
test = f["subgroup"]
f.create_dataset('subgroup3/dataset_three', (10,), dtype='i')

test2 = test["another_dataset"]

for name in f:
    print(name)

dset.attrs['temperature'] = 99.5