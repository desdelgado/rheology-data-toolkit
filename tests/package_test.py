# %%
from rheodata.extractors import antonpaar
from rheodata import data_converter
import h5py
import pandas as pd

rheometer = antonpaar.AntonPaarExtractor()

multi_file_test = "C:/Users/Delgado/Documents/Research/rheology-data-toolkit/tests/test_data/Anton_Paar/excel_test_data/two_tests_Steady State Viscosity Curve-LO50C_excel.xlsx"
output_folder = "C:/Users/Delgado/Documents/Research/rheology-data-toolkit/tests/test_data/Anton_Paar/test_output"


modified_dict, test_raw, cols_info = rheometer.import_rheo_data(multi_file_test)

converter = data_converter.rheo_data_transformer(modified_dict, test_raw, cols_info)
# Test if you can get a dataframe

test = rheometer.make_analyze_dataframes(multi_file_test)

rheometer.save_analyze_dataframes(multi_file_test, output_folder_path=output_folder)

converter.load_to_hdf('CHIMAD_Demo_Demo')

f = h5py.File('CHIMAD_Demo.hdf5', "r")
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

# %%

path = "C:/Users/Delgado/Documents/Research/rheology-data-toolkit/test_data/ARES_G2/temperature_ramp/Copy of Siqi_Temp Ramp.xls"

ARES = ARES_G2Extractor(path)

modified_output, raw_output, cols_info = ARES.process_workbook()

# %%

# %%

path = "C:/Users/Delgado/Documents/Research/rheology-data-toolkit/test_data/ARES_G2/mixed_test_types/Copy of JeT_5k100-5k100_100mgml_amp_frq_swp_672017 copy.xls"

ARES = ARES_G2Extractor(path)

modified_output, raw_output, cols_info = ARES.process_workbook()