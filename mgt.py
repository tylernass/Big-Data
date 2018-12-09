# Description: Used to migrate ~25 .zip files from a central repository to an individual repository

# MIGRATE SCRIPT
import os
loc = "/tartarus/tylernass" # This is the "individual repository"
nw = "/tartarus/DATASETS/SmartMeterData" # Tis is the "central repository"

a = -
def migrate(loc):
    global a
    for i in os.listdir():
        loc = loc + str(i)
        shutil.move("/tartarus/DATASETS/SmartMeterData", loc)
        a += 1
     crtdir(loc)

# CREATE DIRECTORY SCRIPT
def crtdir(loc):
    global a
    for i in range(0, a):
        os.mkdir(loc + str(a))
