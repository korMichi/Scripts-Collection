import os
import shutil

path_to_files = ""
path_to_save = ""


for root, dirs, files in os.walk(path_to_files, topdown=False):
    for name in files:
        if ".ab1" in name:  # extracts files with ab1 in filename
            shutil.copy(os.path.join(root, name), path_to_save)
