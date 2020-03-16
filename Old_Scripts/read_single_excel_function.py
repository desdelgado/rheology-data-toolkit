import pandas as pd  

def read_single_excel(temp_data):
    '''
        Intakes dataframe from anton par and returns a csv with 
        just the data in it

        param: temp_data - data frame from anton par rheometer
    '''

    # Find the index where 'Point No.' occurs so it can be used to 
    # reshape the dataframe
    start_row_index = 0

    # TODO come back and make this not a loop

    for temp_index in range(0, len(temp_data)):
        if str(temp_data.iloc[temp_index,0]) == 'Interval data:':
            start_row_index = temp_index
        # Find the name of the test for later use
        elif (temp_data.iloc[temp_index,0]) == 'Test:':
            test_name = temp_data.iloc[temp_index,1]

    # Reshape the dataframe with just the data
    reshape_data = temp_data.iloc[start_row_index:, 1:]

    # TODO keep track of the units
    unit_columns = []
    # Add the unit to the first line and then make it the column names
    for i in range(0, len(reshape_data.iloc[0,:])):

        unit = str(reshape_data.iloc[2,i])
        header = str(reshape_data.iloc[0,i])
        # If the third row doesn't have units
        #print(str(unit))
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
    reshape_data.to_csv(test_name + '.csv', index=False)