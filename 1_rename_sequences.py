import os
import pandas as pd


def load_filenames(filename):
    """
    Loads names of files from excel sheet into pandas Dataframe
    """
    file_names = pd.read_excel(filename, sheet_name="Plate Name")
    file_names = file_names.set_index("Well Position")  # first column
    return file_names


def rename(name_frame):
    """
    Renames all files in directory with pandas Dataframe
    """
    path_to_files = "/home/michael/Downloads/Order_11106888442-1_Results/plate_NGS Plate 4 LC"  # path of files for renaming
    for files in os.listdir(path_to_files):
        file = files.split("1.")  # split filename and fileextension
        file_extensions = file[1]
        file_name = file[0].replace("_", "")
        if file_name in name_frame.index:  # check if filename is in Dataframe
            new_name = str(name_frame.loc[file_name]["renamed"] + "." + file_extensions)
            os.rename(os.path.join(path_to_files, files), os.path.join(path_to_files, new_name))


name_frame = load_filenames("eblocks-plate_NGS_LCs.xlsx")  # name of excel file
rename(name_frame)