import pandas as pd
import h5py
import json


def add_cols_info(file_path:str):
    """Adds column information to the cleaned data in a HDF5 file produced from
       "rheodata" packge"
       Args:
        file_path (str): File path to HDF5 file
       Returns:
        plot_data (dict): Dictionary of the data as pandas dataframes.
         The test names are the keys
    """
    f = h5py.File(file_path, "r") # Load the data

    plot_data = {}  # Dict to hold the data

    test_keys = f["Project"].keys() # Get the test names

    for test in test_keys:
            test_path = 'Project/' + test + '/clean_data'
            temp_clean_data = pd.read_hdf(file_path, test_path)
            # Column metadata is in a string that we can format using the json library
            temp_cols_metadata_json = f["Project"][test].attrs["columns"]

            try:
                temp_cols_metadata = json.loads(temp_cols_metadata_json)
                names = temp_cols_metadata["names"]
                units = temp_cols_metadata["units"] # In case we want to add units
                temp_clean_data.columns = names

            except TypeError:  # Incase there were no columns
                print("There doesn't seem to be columns metadata for test:")
                print(test)

            plot_data[test] = temp_clean_data

    f.close()

    return plot_data

example_path = "C:/Users/Delgado/Documents/Research/rheology-data-toolkit/getting_started/saved_data/Demo.hdf5"

test = add_cols_info(example_path)
