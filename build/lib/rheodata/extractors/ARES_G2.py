import pandas as pd
import numpy as np
import os
import sys


class ARES_G2Extractor():
    def __init__(self, workbook_path=None):
        self.workbook_path = workbook_path

    def process_workbook(self):

        self.workbook = pd.read_excel(self.workbook_path, sheet_name=None)

        modified_output_dict = {}
        raw_output_dict = {}
        cols_info_dict = {}
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

        return temp_data.iloc[2:, :]

    def get_raw_data(self, page_name):
        temp_data = temp_data = self.workbook[page_name]
        temp_row = pd.DataFrame(
            [[np.nan] * temp_data.shape[1]], columns=temp_data.columns)
        temp_row.iloc[0, 0] = page_name
        temp_data = pd.concat([temp_row, temp_data])
        return temp_data

    def get_col_info(self, page_name):
        temp_data = self.workbook[page_name]

        cols = temp_data.iloc[0, :]
        units = temp_data.iloc[1, :].fillna("", axis=0)
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
