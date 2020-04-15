from rheodata.extractors.antonpaar import AntonPaarExtractor
from rheodata.extractors.data_converter import rheo_data_transformer

import unittest
import pandas as pd
import h5py
import os

extractor = AntonPaarExtractor()
#converter = data_converter()

class TestAntonPaar(unittest.TestCase):

    def setUp(self):
        self.multi_file_test = "C:/Users/Delgado/Documents/Research/rheology-data-toolkit/tests/test_data/Anton_Paar/excel_test_data/two_tests_Steady State Viscosity Curve-LO50C_excel.xlsx"

        self.modified_dict, self.raw_data_dict, self.cols = extractor.import_rheo_data(self.multi_file_test)

        # Inilize the class to convert
        self.converter = rheo_data_transformer(self.modified_dict, self.raw_data_dict, self.cols)
        self.converter.load_to_hdf("test")

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
    
    def test_hdf5_created(self):
        name, ext = os.path.splitext("test.hdf5")
        self.assertEqual(ext, ".hdf5")
    
    def test_project_subfolders_added(self):
        f = h5py.File('test.hdf5', "r")
        project_keys = list(f['Project'].keys())
        f.close()
        self.assertListEqual(project_keys, ['Steady State Viscosity Curve-75C','Steady State Viscosity Curve-LO80C', ])
    
    def test_analyze_cols(self):
        temp_df = extractor.make_analyze_dataframes(self.multi_file_test)

        for test_key in temp_df.keys():
            test_cols = list(temp_df[test_key].columns)
            parsed_cols = list(self.cols[test_key])

            self.assertListEqual(test_cols, parsed_cols)

    # TODO Write test for saving a file
    
if __name__ == '__main__':
    unittest.main()

