# Description: Script to delete repeat files in a directory
loc = "/tartarus/tylernass" # NOTE: This is the location of the script, for every nth directory
# Example location "/tartarus/tylernass/1", "/tartarus/tylernass/2", ... "/tartarus/tylernass/n"

def dlt():
    for i in os.listdir():
        if i[-3:] == "zip":
            os.remove(i) 
