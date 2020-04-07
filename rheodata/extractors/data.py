# %%
import h5py
import pandas as pd
from antonpaar import AntonPaarExtractor as APE
import tables
import os
# %%

class rheo_data_transformer():

    def __init__(self, modified_data, raw_data, cols_info):
        self.modified_data = modified_data
        self.raw_data = raw_data
        self.cols_info = cols_info

        # TODO add different metadata to each test

    def load_to_hdf(self, save_file_name, metadata=None):
        tables.file._open_files.close_all()
        full_file_name = save_file_name + ".hdf5"

        if os.path.exists(full_file_name):
            # TODO figure out how to close file if open
            os.remove(full_file_name)
        
        for clean_key, raw_key in zip(self.modified_data.keys(), self.raw_data.keys()):
            test_path = "Project/" + str(clean_key)

            clean_key_path = test_path + "/clean_data"
            raw_key_path = test_path + "/raw_data"


            self.modified_data[clean_key].to_hdf(full_file_name, key=clean_key_path, mode='a')
            self.raw_data[raw_key].to_hdf(full_file_name, key=raw_key_path, mode='a')

            self.add_test_metadata(full_file_name, metadata, test_path, clean_key)


    def add_project_metadata(self, file_name, metadata):
        
        with h5py.File(file_name, "a") as f:

            for key in metadata.keys():
                f.attrs[key] = metadata[key]

    def add_test_metadata(self, file_name, test_metadata, test_path, test_name):

        #subgroup_path = "/" + test_path
        with h5py.File(file_name, "a") as f:
            for key in test_metadata.keys():
                if key != 'column':
                    f[test_path].attrs[key] = test_metadata[key]
                else:
                    # Load in the right cols according to
                    f[test_path].attrs[key] = test_metadata[self.cols_info[test_name]]