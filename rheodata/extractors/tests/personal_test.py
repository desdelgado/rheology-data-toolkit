#%%

import sys, os
sys.path.append("C:/Users/Delgado/Documents/Research/rheology-data-toolkit/rheodata/extractors")


import pandas as pd
from antonpaar import AntonPaarExtractor as APE
from data import rheo_data_transformer

# %%
extractor = APE()

multi_file_test = "/Users/Delgado/Documents/Research/rheology-data-toolkit/rheodata/extractors/test_data/excel_test_data/Steady State Viscosity Curve-LO50C_excel.xlsx"
output_folder = "/Users/Delgado/Documents/Research/chimad_project/rheodata/extractors/test_data/"


modified_dict, test_raw, cols_info = extractor.import_rheo_data(multi_file_test)

test = rheo_data_transformer(modified_dict, test_raw, cols_info)



test_metadata = {
    "Temperature":25,
    "Test Type": "Strain Sweep",
    "Polyanion_MW":100000,
    "Polycation_MW": 100000,
    "Polyanion_Charge_Fraction": 100,
    "Polycation_Charge_Fraction": 100,
    "Salt_Type": "potassium bromide",
    "Salt_Concentration": 10,
    "Solvent": "water",
    "Solvent_concentration":25,
    "columns":[]
}


test.load_to_hdf("test3", test_metadata)
# %%

project_metadata = {
    'Author': 'David Delgado',
    'Test_Type': "Strain Sweep",
    'Polyanion': 'polystyrene sulfonate',
    'Polycation': 'poly (4-vinylpyridine)'
}

test.add_project_metadata("test3.hdf5", metadata)

# %%
f = h5py.File('test3.hdf5', "r")
# %%
f.attrs["name"]
test = pd.read_hdf('swag.h5', 'top/Steady State Viscosity Curve/clean_data')
# %%
f.close()


# %%   ###### TESTS #######
failed_count=0
for key in test_raw.keys():
        df = test_raw[key]
        if df.iloc[0,0] != 'Project:':

            print('test_failed')
            print(key)
            failed_count += 1

if failed_count == 0:
    print("Test Passed")
else:
    print(failed_count)

# %%
failed_count=0
for key in test_raw.keys():
        df = test_raw[key]
        if df.iloc[1,0] != 'Test:':

            print('test_failed')
            print(key)
            failed_count += 1

if failed_count == 0:
    print("Test Passed")
else:
    print(failed_count)




# %%