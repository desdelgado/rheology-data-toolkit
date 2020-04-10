# %%
from rheodata.extractors import antonpaar, data_converter
import h5py
import pandas as pd


rheometer = antonpaar.AntonPaarExtractor()

multi_file_test = "C:/Users/Delgado/Documents/Research/rheology-data-toolkit/test_data/excel_test_data/two_tests_Steady State Viscosity Curve-LO50C_excel.xlsx"
output_folder = "/Users/Delgado/Documents/Research/chimad_project/rheodata/extractors/test_data/"


modified_dict, test_raw, cols_info = rheometer.import_rheo_data(multi_file_test)

converter = data_converter.rheo_data_transformer(modified_dict, test_raw, cols_info)

converter.load_to_hdf('Shull_Group_Demo')

f = h5py.File('Shull_Group_Demo.hdf5', "r")
print(f["Project"].keys())
print(f["Project"]['Steady State Viscosity Curve-75C'].keys())

raw_data = pd.read_hdf('Shull_Group_Demo.hdf5', 'Project/Steady State Viscosity Curve-75C/raw_data')
print(raw_data.head(10))
f.close()

project_metadata = {
    "Project_Name": "Shull Group Demo",
    'Author': 'David Delgado',
    "Doi": "https//8675309",
    'Test_Type': "Strain Sweep",
    'Polymer': ['polystyrene sulfonate', 'poly (4-vinylpyridine)'],
    "Instrument": "Anton Paar MCR32"
}

converter.add_project_metadata("Shull_Group_Demo.hdf5", project_metadata)

f = h5py.File('Shull_Group_Demo.hdf5', "r")
print(f.attrs["Project_Name"])
print(f.attrs["Author"])
print(f.attrs["Doi"])
print(f.attrs["Test_Type"])
print(f.attrs["Polymer"])
print(f.attrs["Instrument"])
f.close()


test_metadata = {
    'Steady State Viscosity Curve-LO80C':
    {
    "Temperature":80,
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
    "Temperature":75,
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

converter.add_test_metadata(test_metadata)

f = h5py.File('Shull_Group_Demo.hdf5', "r")
print(f["Project/Steady State Viscosity Curve-75C"].attrs["Temperature"])
print(f["Project/Steady State Viscosity Curve-LO80C"].attrs["Temperature"])

print(f["Project/Steady State Viscosity Curve-75C"].attrs["Polyanion_MW"])
print(f["Project/Steady State Viscosity Curve-LO80C"].attrs["Polyanion_MW"])

f.close()