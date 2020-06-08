#%%

import sys, os
sys.path.append("C:/Users/Delgado/Documents/Research/rheology-data-toolkit/rheodata/extractors")

import h5py
import pandas as pd
from antonpaar import AntonPaarExtractor as APE
from ARES_G2 import ARES_G2Extractor 
# %%
sys.path.append("C:/Users/Delgado/Documents/Research/rheology-data-toolkit/rheodata")
from data_converter import rheo_data_transformer

# %%

# %%
machine = APE()

multi_file_test = "C:/Users/Delgado/Documents/Research/rheology-data-toolkit/tests/test_data/Anton_Paar/excel_test_data/Steady State Viscosity Curve-LO50C_excel.xlsx"
output_folder = "/Users/Delgado/Documents/Research/chimad_project/rheodata/extractors/test_data/"


modified_dict, test_raw, cols_info, units_info = machine.import_rheo_data(multi_file_test)
# %%
test = rheo_data_transformer(modified_data=modified_dict, raw_data=test_raw, cols_info=cols_info, units=units_info)

test.load_to_hdf('hdf5_pickle_fix')

# %%
f = h5py.File("hdf5_pickle_fix.hdf5", "r")
print(f["Project"].keys())
print(f["Project"]['Steady State Viscosity Curve-55C'].keys())
print(type(f["Project"]['Steady State Viscosity Curve-55C'].attrs["columns"]))

test = f["Project"]['Steady State Viscosity Curve-55C'].attrs["columns"]

raw_data = pd.read_hdf('hdf5_pickle_fix.hdf5', 'Project/Steady State Viscosity Curve-55C/clean_data')
print(raw_data.head(10))
f.close()

f = h5py.File(save_file_name +'.hdf5', "r")
print(f.attrs["Project_Name"])
print(f.attrs["Author"])
print(f.attrs["Doi"])
print(f.attrs["Test_Type"])
print(f.attrs["Polymer"])
print(f.attrs["Instrument"])
f.close()

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
# %%  #### ARES tests ####

path = "C:/Users/Delgado/Documents/Research/rheology-data-toolkit/tests/test_data/ARES_G2/mixed_test_types/Copy of JeT_5k100-5k100_100mgml_amp_frq_swp_672017 copy.xls"

ARES = ARES_G2Extractor(path)

modified_output, raw_output, cols_info, units_info = ARES.process_workbook()


test = rheo_data_transformer(modified_data=modified_output, raw_data=raw_output, cols_info=cols_info, units=units_info)

test.load_to_hdf('AGRES_2_test')

f = h5py.File("test_package.hdf5", "r")
print(f["Project"].keys())
print(f["Project"]['Temperature Ramp - 1'].keys())



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