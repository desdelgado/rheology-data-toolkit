# %%
from rheodata.extractors import antonpaar, data_converter
import h5py
import pandas as pd
# %%

machine = antonpaar.AntonPaarExtractor()

multi_file_test = "C:/Users/Delgado/Documents/Research/rheology-data-toolkit/test_data/excel_test_data/Steady State Viscosity Curve-LO50C_excel.xlsx"
output_folder = "/Users/Delgado/Documents/Research/chimad_project/rheodata/extractors/test_data/"


modified_dict, test_raw, cols_info = machine.import_rheo_data(multi_file_test)

test = data_converter.rheo_data_transformer(modified_dict, test_raw, cols_info)

# %% 

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

test.add_project_metadata("test3.hdf5", project_metadata)

# %%
f = h5py.File('test3.hdf5', "r")
# %%
f.attrs["name"]
# %%
test = pd.read_hdf('test3.hdf5', 'Project/Steady State Viscosity Curve/raw_data')
# %%
f.close()
