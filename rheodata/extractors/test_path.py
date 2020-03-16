from antonpaar import AntonPaarExtractor

extractor = AntonPaarExtractor()

path = r"Users/Delgado/Documents/!Research/chimad_project/rheodata/extractors/test_data/excel_test_data/Steady State Viscosity Curve-LO50C_excel.xlsx"
# Enter the realtive path to the folder you wish to output your data to
output_folder_path = r"Users/Delgado/Documents/!Research/chimad_project/rheodata/extractors/test_data/"

test = extractor.import_rheo_data(path, output_folder_path)


print(test)