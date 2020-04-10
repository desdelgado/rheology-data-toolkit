
from rheodata.extractors.antonpaar import AntonPaarExtractor

import unittest
import pandas as pd

extractor = AntonPaarExtractor()

class TestAntonPaar(unittest.TestCase):

    def setUp(self):
        self.multi_file_test = "C:/Users/Delgado/Documents/Research/rheology-data-toolkit/test_data/Anton_Paar/excel_test_data/Steady State Viscosity Curve-LO50C_excel.xlsx"

        self.modified_dict, self.raw_data_dict, self.cols = extractor.import_rheo_data(self.multi_file_test)

    def test_modified_output_isdictionary(self):

        self.assertIsInstance(self.modified_dict, dict)

    def test_modified_output_dictionary_contains_pandas(self):
        """ Test if the output is a dictonary of pandas dataframes'"""

        for value in self.modified_dict.values():
            self.assertIsInstance(value, pd.DataFrame)

    def test_raw_output_isdictionary(self):

        self.assertIsInstance(self.raw_data_dict, dict)

    def test_raw_output_dictionary_contains_pandas(self):
        """ Test if the output is a dictonary of pandas dataframes'"""
        for value in self.raw_data_dict.values():
            self.assertIsInstance(value, pd.DataFrame)

    def test_project_name_added_raw_data(self):
        """ Test if the output is a dictonary of pandas dataframes'"""
        for df in self.raw_data_dict.values():
            self.assertEqual(df.iloc[0,0], "Project:")
            

if __name__ == '__main__':
    unittest.main()

