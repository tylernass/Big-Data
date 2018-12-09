# Python script used to unzip (.zip) files from a databases

# Function: Script used to unzip files in the desired directory, whether it is a zip or a csv.zip file
# Question: When/how do I define a base case for this function?
import os, zipfile, shutil
def zip():
    for i in os.listdir():
        zip = zipfile.ZipFile(i)
        zip.extractall()
    zip()


# TO be run in directory: SmartMeterData

# Function: Script to migrate data from /tartarus/DATASETS/SmartMeterData to /tartarus/tylernass/n for the respective nth directory, 1-25
# Function must also erase previous .zip files
def migrate():
    for i in os.listdir():
        loc = "/tartarus/tylernass" + str(i)
        shutil.move("/tartarus/DATASETS/SmartMeterData", loc)


x = input("1. Unzip files in a directory\n2. Migrate data\n")
if x == 1:
    zip()

if x == 2:
    migrate()

    # /tartarus/tylernass
    # /tartarus/tylernass


    # PLAN: Migrate ALL of the unnzipped folders to /tartarus/tylernass/n and run the commands there
    # Create 25 directories for EACH unzipped folder
    # Create a script to parse the CSV
