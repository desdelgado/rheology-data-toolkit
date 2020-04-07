
from rheodata.extractors.antonpaar import AntonPaarExtractor

import unittest
import pandas as pd
# %%


extractor = AntonPaarExtractor()

class TestAntonPaar(unittest.TestCase):

    def setUp(self):
        self.multi_file_test = "/Users/Delgado/Documents/Research/rheology-data-toolkit/rheodata/extractors/test_data/excel_test_data/Steady State Viscosity Curve-LO50C_excel.xlsx"
        self.output_folder = "/Users/Delgado/Documents/Research/chimad_project/rheodata/extractors/test_data/"

        self.txtfile = "/Users/Delgado/Documents/Research/rheology-data-toolkit/rheodata/extractors/test_data/gwens_data/Steady State Viscosity Curve-LO80C_txt.txt"
        self.csvfile = "/Users/Delgado/Documents/Research/rheology-data-toolkit/rheodata/extractors/test_data/gwens_data/Steady State Viscosity Curve-35C.csv"
        self.xmlfile = "/Users/Delgado/Documents/Research/rheology-data-toolkit/rheodata/extractors/test_data/gwens_data/Steady State Viscosity Curve-LO80C_xml.xml"

    def test_modified_output_isdictionary(self):
        modified_dict, raw_data_dict = extractor.import_rheo_data(self.multi_file_test, self.output_folder)

        self.assertIsInstance(modified_dict, dict)


    def test_modified_output_dictionary_contains_pandas(self):
        """ Test if the output is a dictonary of pandas dataframes'"""
        modified_dict, raw_data_dict = extractor.import_rheo_data(self.multi_file_test, self.output_folder)

        for value in modified_dict.values():
            self.assertIsInstance(value, pd.DataFrame)

    def test_raw_output_isdictionary(self):
        modified_dict, raw_data_dict = extractor.import_rheo_data(self.multi_file_test, self.output_folder)

        self.assertIsInstance(raw_data_dict, dict)

    def test_raw_output_dictionary_contains_pandas(self):
        """ Test if the output is a dictonary of pandas dataframes'"""
        modified_dict, raw_data_dict = extractor.import_rheo_data(self.multi_file_test, self.output_folder)

        for value in raw_data_dict.values():
            self.assertIsInstance(value, pd.DataFrame)

    def test_project_name_added_raw_data(self):
        """ Test if the output is a dictonary of pandas dataframes'"""
        modified_dict, raw_data_dict = extractor.import_rheo_data(self.multi_file_test, self.output_folder)

        for df in raw_data_dict.values():
            self.assertEqual(df.iloc[0,0], "Test:")
            
    


if __name__ == '__main__':
    unittest.main()

