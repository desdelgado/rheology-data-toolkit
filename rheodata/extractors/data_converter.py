# %%
import h5py
import pandas as pd
from antonpaar import AntonPaarExtractor as APE
import tables
import os
# %%
class rheo_data_transformer():

    def __init__(self, modified_data=None, raw_data=None, cols_info=None):
        self.modified_data = modified_data
        self.raw_data = raw_data
        self.cols_info = cols_info
        self.full_file_name = ''

        # TODO add different metadata to each test

    def load_to_hdf(self, save_file_name, metadata=None):
        tables.file._open_files.close_all()
        self.full_file_name = save_file_name + ".hdf5"

        if os.path.exists(self.full_file_name):
            # TODO figure out how to close file if open
            os.remove(self.full_file_name)
        
        for clean_key, raw_key in zip(self.modified_data.keys(), self.raw_data.keys()):
            test_path = "Project/" + str(clean_key)

            clean_key_path = test_path + "/clean_data"
            raw_key_path = test_path + "/raw_data"


            self.modified_data[clean_key].to_hdf(self.full_file_name, key=clean_key_path, mode='a')
            self.raw_data[raw_key].to_hdf(self.full_file_name, key=raw_key_path, mode='a')

            #self.add_test_metadata(self.full_file_name, metadata, test_path, clean_key)


    def add_project_metadata(self, file_name, metadata):
        
        with h5py.File(file_name, "a") as f:

            for key in metadata.keys():
                f.attrs[key] = metadata[key]

    def add_test_metadata(self, test_metadata):

        with h5py.File(self.full_file_name, "a") as f:

            # Navigate through the different tests in the HDF5
            for test_key in self.modified_dict.keys():
                test_path = "Project/" + str(test_key)
                
                # Look through the keys in the test_metadata
                for metadata_test_key in test_metadata.keys():

                    # If the metadata test tkey key matches the name of the test name
                    if test_key == metadata_test_key:
                        # Load the attributes in that tests metadata 
                        for attr_keys in test_metadata[metadata_test_key].keys():

                            if attr_keys != 'column':
                                f[test_path].attrs[attr_keys] = test_metadata[metadata_test_key][attr_keys]
                            else:
                                # Load in the right cols according to
                                f[test_path].attrs[attr_keys] = test_metadata[metadata_test_key][self.cols_info[metadata_test_key]]