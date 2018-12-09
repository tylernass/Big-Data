# Description: Script to open zipped files in a directory

import os, zipfile
loc = "/tartarus/tylernass" # In this location, there are n directories (where n = # of zip files)
# Example location: "/tartarus/tylernass/1", "/tartarus/tylernass/2", ... "/tartarus/tylernass/n"

# UNZIP SCRIPT
def zip():
     for i in os.listdir():
         if i[-7:] == "csv.zip":
                     zp = zipfile.ZipFile(i)
                     zp.extractall()
