# %%
import h5py
import pandas as pd
import tables
import os
import json

import pickle

# %%
class rheo_data_transformer():
    """Organizes rheology dictionaries into HDF5 file"""

    def __init__(self, modified_data:dict=None, raw_data:dict=None,
     cols_info:dict=None, units:dict=None):
        pickle.HIGHEST_PROTOCOL = 4

        self.modified_data = modified_data
        self.raw_data = raw_data
        self.cols_info = cols_info
        self.full_file_name = ''
        self.units = units

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
        self.add_cols_metadata()

    def add_cols_metadata(self):
           with h5py.File(self.full_file_name, "a") as f:
            # Navigate through the different tests in the HDF5
            for test_key in self.modified_data.keys():
                test_path = "Project/" + str(test_key)
                colum_metadata = {
                    'names': self.cols_info[test_key],
                    'units': self.units[test_key]
                    }

                colum_metadata = json.dumps(colum_metadata)

                f[test_path].attrs['columns'] = colum_metadata

class add_rheo_metadata():
    """Adds metadata to files"""

    def __init__(self, file_path:str=None):
        self.file_path = file_path

    # TODO figure out where to optimal place to put this is
    def add_project_metadata(self, metadata):
        project_metadata = json.dumps(metadata)

        with h5py.File(self.file_path, "a") as f:
            f["Project"].attrs["project_metadata"] = project_metadata
    
    def add_test_metadata(self, test_name:str, test_metadata):
        """Adds metadata to one test subfolder"""
        test_metadata = json.dumps(test_metadata)

        with h5py.File(self.file_path, "a") as f:
            try:
                f["Project"][test_name].attrs["test_metadata"] = test_metadata
            except: # Temp hold while I figure out a better way to do this
                print("Didn't add metadata for:" + test_name)

        