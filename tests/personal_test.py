#%%

import sys, os
sys.path.append("C:/Users/Delgado/Documents/Research/rheology-data-toolkit/rheodata/extractors")


import pandas as pd
from antonpaar import AntonPaarExtractor as APE
from data import rheo_data_transformer

# %%

# %%
machine = APE()

multi_file_test = "C:/Users/Delgado/Documents/Research/rheology-data-toolkit/test_data/excel_test_data/two_tests_Steady State Viscosity Curve-LO50C_excel.xlsx"
output_folder = "/Users/Delgado/Documents/Research/chimad_project/rheodata/extractors/test_data/"


modified_dict, test_raw, cols_info = machine.import_rheo_data(multi_file_test)

test = rheo_data_transformer(modified_dict, test_raw, cols_info)

test.load_to_hdf('swag')

# %% 
test_metadata = {
    'Steady State Viscosity Curve-LO80C':
    {
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
    },

    'Steady State Viscosity Curve-75C':
    {
    "Temperature":100,
    "Test Type": "Freq Sweep",
    "Polyanion_MW":500,
    "Polycation_MW": 5000,
    "Polyanion_Charge_Fraction": 100,
    "Polycation_Charge_Fraction": 100,
    "Salt_Type": "potassium bromide",
    "Salt_Concentration": 20,
    "Solvent": "water",
    "Solvent_concentration":10,
    "columns":[]
    }
}

# %%
test.add_test_metadata(test_metadata)


# %%
file_path = "C:/Users/Delgado/Documents/Research/rheology-data-toolkit/rheodata/extractors/swag.hdf5"

f = h5py.File(file_path, "r")

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