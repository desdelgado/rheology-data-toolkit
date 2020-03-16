import pandas as pd 

############### User Inputs ###############
# Give the realative path to the file here 
### Must be an xlsx file ###
path = "test_data/excel_test_data/Steady State Viscosity Curve-LO50C_excel.xlsx"
# Enter the realtive path to the folder you wish to output your data to
output_folder_path = "test_data/test_output/"
###########################################

def read_single_excel(temp_data, output_folder:str):
    '''
    Intakes dataframe from anton par and returns a csv with 
    just the data in it

    param: temp_data - data frame from anton par rheometer
    '''
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

    # Save to a CSV file with the test name
    reshape_data.to_csv(output_folder + test_name + '.csv', index=False)


temp_data = pd.read_excel(path)
        
test_indexes = temp_data.index[temp_data.iloc[:,0]== 'Test:'].tolist()

for i in range(len(test_indexes)):
    #test_index = int(i)
    # Test if were not the last one
    if test_indexes[i] != test_indexes[-1]:
        # Get the next index
        next_data_index = int(test_indexes[i+1]) - 1
        temp_df = temp_data.iloc[test_indexes[i]:next_data_index,:]

        # Parse just the data
        read_single_excel(temp_df, output_folder_path)

    # If it's the last number in the list
    else:
        
        temp_df = temp_data.iloc[i:,:]
        read_single_excel(temp_df, output_folder_path)