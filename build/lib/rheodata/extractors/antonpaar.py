# %%

import pandas as pd
import sys
import os


# %%
class AntonPaarExtractor():
    def __init__(self):
        self.test_names = []
        """ I believe I dont need this"""

    def import_rheo_data(self, input_path: str):
        """
        Intakes the input path of the xlsx file from the user and returns
        dictionary with each test from xlsx file as a dataframe as the value
        and the testname as the key
        """
        temp_data = pd.read_excel(input_path, header=None)
        project_row = temp_data[temp_data.iloc[:, 0] == 'Project:']
        # Get the project from the top of the data
        test_indexes = temp_data.index[temp_data.iloc[:, 0] == 'Test:'].tolist(
        )
        # create a dictionary to hold the dataframes from the xslx file
        modified_output_dict = {}
        raw_output_dict = {}
        cols_info_dict = {}
        units_dict = {}
        for i in range(len(test_indexes)):

            # Test if were not the last one
            if test_indexes[i] != test_indexes[-1]:

                # Get the next index
                test_start_index = test_indexes[i]
                test_end_index = int(test_indexes[i+1]) - 1
                raw_df = temp_data.iloc[test_start_index:test_end_index, :]

                cleaned_df, test_name, cols_info, units_info = self.process_single_excel(
                    raw_df)

                modified_output_dict[test_name] = cleaned_df
                raw_output_dict[test_name] = pd.concat([project_row, raw_df])
                cols_info_dict[test_name] = cols_info
                units_dict[test_name] = units_info

                self.test_names.append(test_name)

            # If it's the last number in the list
            else:
                test_start_index = int(test_indexes[i])
                raw_df = temp_data.iloc[test_start_index:, :]

                cleaned_df, test_name, cols_info, units_info = self.process_single_excel(
                    raw_df)

                modified_output_dict[test_name] = cleaned_df
                raw_output_dict[test_name] = pd.concat([project_row, raw_df])
                cols_info_dict[test_name] = cols_info
                units_dict[test_name] = units_info

                self.test_names.append(test_name)

        # Pass back a dictionary of dataframes
        return modified_output_dict, raw_output_dict, cols_info_dict, units_dict

    def process_single_excel(self, temp_data):
        """
        Intakes dataframe from anton par and returns a csv with 
        just the data in it as well as the test name.  
        Also has option to save the data to a given output folder 

        param: temp_data - data frame from anton par rheometer
        """
        # Find the index where 'Point No.' occurs so it can be used to
        # reshape the dataframe
        start_row_index = 0

        temp_data = temp_data.reset_index(drop=True)
        # Find where the data starts
        start_row_index = temp_data.index[temp_data.iloc[:, 0] == 'Interval data:'].tolist()[
            0]
        # Test name - used later when program is extended to multiple tests
        test_index = temp_data.index[temp_data.iloc[:, 0] == 'Test:'].tolist()[
            0]
        test_name = temp_data.iloc[test_index, 1]

        # Reshape the dataframe with just the data
        reshape_data = temp_data.iloc[start_row_index:, 1:]

        # TODO keep track of the units
        col_names = []
        units = []
        # Add the unit to the first line and then make it the column names
        for i in range(0, len(reshape_data.iloc[0, :])):
            unit = str(reshape_data.iloc[2, i])
            col = str(reshape_data.iloc[0, i])

            # If the third row doesn't have units
            if unit != 'nan':
                # Add the units
                col_names.append(col)
                units.append(unit)
            else:
                col_names.append(col)
                units.append('NaN')

        # Set the Columns to the first row and remove the first row
        reshape_data = reshape_data.iloc[3:, :].reset_index(drop=True)

        self.parse_test_type(reshape_data)

        return reshape_data, test_name, col_names, units

    def check_file_type(self, path):
        """ Check what type of file it is"""
        name, ext = os.path.splitext(path)
        if ext == '.xlsx':
            return True
        else:
            return False

    def save_analyze_dataframes(self, file_path, output_folder_path: str = ''):
        analyze_dict = self.make_analyze_dataframes(file_path)

        for test_key in analyze_dict.keys():
            temp_df = analyze_dict[test_key]

            save_path = output_folder_path + "/" + test_key + ".csv"

            temp_df.to_csv(save_path)

    def make_analyze_dataframes(self, path):
        modified_data, raw_data, cols, units = self.import_rheo_data(path)

        # Need to link the cols to the file
        analyze_dict = {}
        for test in list(modified_data.keys()):
            temp_df = modified_data[test]
            temp_df.columns = cols[test]
            analyze_dict[test] = temp_df

        return analyze_dict

    def parse_test_type(self, raw_df):
        """
        Look at the columns of the inputed data and determine
        what type of plots to plot 
        """
        # Get the columns
        cols = raw_df.columns
        # List of variables that uniquely identify what type of data it is
        freq_sweel_list = ['Angular Frequency [rad/s]',
                           'Storage Modulus [Pa]', 'Loss Modulus [Pa]']
        amplitude_sweep = ['Shear Strain [1]',
                           'Storage Modulus [Pa]', 'Loss Modulus [Pa]']

        # Check if its a frequency sweep
        if all(elem in cols for elem in freq_sweel_list):
            print("Frequency Sweep")
            # return 'freq_sweep'
        # Check if its an amplitude sweep
        elif all(elem in cols for elem in amplitude_sweep):
            print("Amplitude Sweep")
            # return "amplitude_sweep"

    def print_test_names(self):
        if self.test_names == []:
            print("No data loaded")
        else:
            print(self.test_names)

    def version(self) -> str:
        return '0.0.1'