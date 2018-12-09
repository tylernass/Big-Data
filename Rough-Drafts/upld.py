# Description: Script sed to upload more data to the database

import os
import glob

path = '/Users/tylernass/Desktop/energy-research/features'
conn_mysql = MySQLdb.connect(host = "chaos.cs.uchicago.edu",user = "tylernass",passwd="Gorregated814$")
cursor_mysql = conn_mysql.cursor()
table_to_use = ""
for filename in glob.glob( os.path.join(path, '*.txt') ):
    currentfile = open(filename, 'r')
    for line in currentfile[1:]:
        insert_data_to_database(line, table_to_use)
        #use the above function to insert data based on the table_to_use
