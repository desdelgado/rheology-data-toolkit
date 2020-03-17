from rheodata.extractors.antonpaar import AntonPaarExtractor

extractor = AntonPaarExtractor()

path = "/Users/Delgado/Documents/Research/rheology-data-toolkit/rheodata/extractors/test_data/excel_test_data/Steady State Viscosity Curve-LO50C_excel.xlsx"
txt_path = "/Users/Delgado/Documents/Research/rheology-data-toolkit/rheodata/extractors/test_data/gwens_data/Steady State Viscosity Curve-LO80C_txt.txt"
# Enter the realtive path to the folder you wish to output your data to
output_folder_path = "/Users/Delgado/Documents/Research/chimad_project/rheodata/extractors/test_data/"

test = extractor.import_rheo_data(txt_path, output_folder_path)

#test = pd.read_excel(path)




print(type(test))

print(type(test['Steady State Viscosity Curve-LO30C']))   