# %%
import pandas as pd
import os
import sys

# %%

# TODO

class ARES_G2Extractor():
    def __init__(self, workbook_path=None):
        self.workbook_path = workbook_path

    def process_raw_data(self):

        self.is_correct_file_type()

        self.workbook = pd.read_excel(self.workbook_path, sheet_name=None)

        modified_output_dict = {}
        raw_output_dict = {}
        cols_info_dict ={}
        for page in self.workbook.keys():
            if page == "Details":
                pass
            else:
                modified_output_dict[page] = self.get_processed_data(page)
                raw_output_dict[page] = self.get_raw_data(page)
                cols_info_dict[page] = self.get_col_info(page)

        return modified_output_dict, raw_output_dict, cols_info_dict

    def get_processed_data(self, page_name):
        temp_data = temp_data = self.workbook[page_name]

        return temp_data.iloc[2:,:]    

    def get_raw_data(self, page_name):
        temp_data = temp_data = self.workbook[page_name]
        temp_series = pd.Series(page_name)
        temp_data = temp_data.append(temp_series)
        return temp_data
                  
    def get_col_info(self, page_name):
        temp_data = self.workbook[page_name]

        cols = temp_data.iloc[0,:]
        units = temp_data.iloc[1,:].fillna("", axis=0)
        col_info = list(cols + " (" + units + ")")

        return col_info

    def is_correct_file_type(self):
        correct_file_type = self.check_file_type()
        if correct_file_type == False:
            print("File is not in raw .xls format")
            print("Stopping program.  Convert file and try again.")
            sys.exit()

    def check_file_type(self):
        """ Check what type of file it is"""
        name, ext = os.path.splitext(self.workbook_path)
        if ext == ".xls":
            return True
        else:
            return False     



# seperate the details file
# For each page of the workbook (key in dictionary)
#   Split into raw data
#   Get just the data and capture the col units

# %%

path = "C:/Users/Delgado/Documents/Research/rheology-data-toolkit/test_data/ARES_G2/temperature_ramp/Copy of Siqi_Temp Ramp.xls"

ARES = ARES_G2Extractor(path)

modified_output, raw_output, cols_info = ARES.process_raw_data()

# %%

# %%

path = "C:/Users/Delgado/Documents/Research/rheology-data-toolkit/test_data/ARES_G2/temperature_ramp/Copy of Siqi_Temp Ramp.xls"


workbook = pd.read_excel(path, sheet_name=None)

# %%
