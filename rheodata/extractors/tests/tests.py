from rheodata.extractors.antonpaar import AntonPaarExtractor

import unittest
import pandas as pd



extractor = AntonPaarExtractor()

class TestAntonPaar(unittest.TestCase):

    def setUp(self):
        self.multi_file_test = "/Users/Delgado/Documents/Research/rheology-data-toolkit/rheodata/extractors/test_data/excel_test_data/Steady State Viscosity Curve-LO50C_excel.xlsx"
        self.output_folder = "/Users/Delgado/Documents/Research/chimad_project/rheodata/extractors/test_data/"

        self.txtfile = "/Users/Delgado/Documents/Research/rheology-data-toolkit/rheodata/extractors/test_data/gwens_data/Steady State Viscosity Curve-LO80C_txt.txt"
        self.csvfile = "/Users/Delgado/Documents/Research/rheology-data-toolkit/rheodata/extractors/test_data/gwens_data/Steady State Viscosity Curve-35C.csv"
        self.xmlfile = "/Users/Delgado/Documents/Research/rheology-data-toolkit/rheodata/extractors/test_data/gwens_data/Steady State Viscosity Curve-LO80C_xml.xml"

    def test_output_dictionary(self):
        test_dict = extractor.import_rheo_data(self.multi_file_test, self.output_folder)

        self.assertIsInstance(test_dict, dict)


    def test_output_dictionary_pandas(self):
        """ Test if the output is a dictonary of pandas dataframes'"""
        test_dict = extractor.import_rheo_data(self.multi_file_test, self.output_folder)

        for value in test_dict.values():
            self.assertIsInstance(value, pd.DataFrame)

            
    '''
    def test_reject_diff_filetypes(self):
        diff_files = [self.txtfile, self.csvfile, self.xmlfile]

        for file in diff_files:
            temp_testfile = extractor.import_rheo_data(file, self.xmlfile)
    '''




 

if __name__ == '__main__':
    unittest.main()

