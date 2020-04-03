#%%

import sys, os
sys.path.append("C:/Users/Delgado/Documents/Research/rheology-data-toolkit/rheodata/extractors")


import pandas as pd
from antonpaar import AntonPaarExtractor as APE

# %%
# %%

extractor = AntonPaarExtractor()

multi_file_test = "/Users/Delgado/Documents/Research/rheology-data-toolkit/rheodata/extractors/test_data/excel_test_data/Steady State Viscosity Curve-LO50C_excel.xlsx"
output_folder = "/Users/Delgado/Documents/Research/chimad_project/rheodata/extractors/test_data/"


modified_dict, test_raw = extractor.import_rheo_data(multi_file_test, output_folder)


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