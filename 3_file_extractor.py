import os
import shutil
import pandas as pd

path_to_files = ""
path_to_save = ""


def load_filenames(filename):
    """
    Loads names of files from excel sheet into pandas Dataframe
    """
    file_names = pd.read_excel(filename, sheet_name="Sheet1")  # enter sheetname
    return file_names


file_names = load_filenames(".xlsx")  # load Excel filename
file_names = file_names[""].to_list()  # name of excel column


for root, dirs, files in os.walk(path_to_files, topdown=False):
    for name in files:
        for extraction_name in file_names:
            if extraction_name in name:
                shutil.copy(os.path.join(root, name), path_to_save)
