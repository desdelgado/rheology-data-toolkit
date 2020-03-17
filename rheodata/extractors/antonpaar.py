import pandas as pd
import sys
import os


class AntonPaarExtractor():
    def __init__(self):
        """ I believe I dont need this"""


    def process_single_excel(self, temp_data, output_folder:str='', save_data:bool=False):
        """
        Intakes dataframe from anton par and returns a csv with 
        just the data in it as well as the test name.  
        Also has option to save the data to a given output folder 

        param: temp_data - data frame from anton par rheometer
        """
        # Find the index where 'Point No.' occurs so it can be used to 
        # reshape the dataframe
        start_row_index = 0
        
        # Reset the index
        temp_data = temp_data.reset_index(drop=True)

        # Find where the data starts
        start_row_index = temp_data.index[temp_data.iloc[:,0] == 'Interval data:'].tolist()[0]
        # Test name - used later when program is extended to multiple tests
        test_index = temp_data.index[temp_data.iloc[:,0] == 'Test:'].tolist()[0]
        test_name = temp_data.iloc[test_index,1]

        # Reshape the dataframe with just the data
        reshape_data = temp_data.iloc[start_row_index:, 1:]

        # TODO keep track of the units
        unit_columns = []
        # Add the unit to the first line and then make it the column names
        for i in range(0, len(reshape_data.iloc[0,:])):
            unit = str(reshape_data.iloc[2,i])
            header = str(reshape_data.iloc[0,i])

            # If the third row doesn't have units
            if unit != 'nan': 
                # Add the units
                unit_header = header + " " + unit
                unit_columns.append(unit_header)
            else:
                unit_columns.append(header)

        # Set the Columns to the first row and remove the first row
        reshape_data.columns = unit_columns
        reshape_data = reshape_data.iloc[3:,:].reset_index(drop=True)

        # Save to a CSV file with the test name if the swtich is true
        if save_data == True:
            reshape_data.to_csv(output_folder + test_name + '.csv', index=False)

        return reshape_data, test_name
    
    def check_file_type(self, path):
        """ Check what type of file it is"""
        name, ext = os.path.splitext(path)
        if ext == '.xlsx':
            return True
        else:
            return False
        
    def import_rheo_data(self, input_path:str, output_folder_path:str=''):
        """
        Intakes the input path of the xlsx file from the user and returns
        dictionary with each test from xlsx file as a dataframe as the value
        and the testname as the key
        """

        # Test to make sure were getting the right path
        correct_filetype = self.check_file_type(input_path)

        if correct_filetype == False:
            print("File is not in .xlsx format")
            print("Stopping program.  Convert file and try again.")
            sys.exit()

        temp_data = pd.read_excel(input_path)
        test_indexes = temp_data.index[temp_data.iloc[:,0]== 'Test:'].tolist()

        # create a dictionary to hold the dataframes from the xslx file
        data_dict = {}
        for i in range(len(test_indexes)):
            # Test if were not the last one
            if test_indexes[i] != test_indexes[-1]:
                # Get the next index
                next_data_index = int(test_indexes[i+1]) - 1
                temp_df = temp_data.iloc[test_indexes[i]:next_data_index,:]

                # Parse just the data
                cleaned_df, test_name = self.process_single_excel(temp_df, output_folder_path)
                data_dict[test_name] = cleaned_df
            # If it's the last number in the list
            else:
                temp_df = temp_data.iloc[i:,:]
                cleaned_df, test_name = self.process_single_excel(temp_df, output_folder_path)
                data_dict[test_name] = cleaned_df
        
        # Pass back a dictionary of dataframes
        return data_dict

    def version(self) -> str:
        return '0.0.1'


