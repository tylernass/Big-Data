# Starting location: /tartarus/DATASETS/SmartMeterData
orig = "/tartarus/DATASETS/SmartMeterData"
loc = "/tartarus/tylernass"

import os, zipfile
import shutil
import math
import datetime
from datetime import datetime, date, time
import csv
from zipfile import ZipFile
import psycopg2

# Function to be ran in orig location "/tartarus/DATASETS/SmartMeterData"
# Step 1: Create directory for the files in loc /tartarus/tylernass, with respect to their names
def mkdr():
    for i in os.listdir():
        nm = i[:6]
        os.mkdir(loc + "/" + str(nm))
    mgt()

# Step 2: Migrate all .zip files in (orig) to (loc)
def mgt():
    for i in os.listdir():
        nw = (loc + "/" + str(i))
        cp = "/tartarus/DATASETS/SmartMeterData/" + str(i)
        shutil.copy2(cp, nw)
    unzpa()

# Step 3: Unzip the 1st .zip files (Ex: 201503.zip)
def unzpa():
    os.chdir(loc)
    for i in os.listdir():
        zf = ZipFile(loc + "/" + str(i) + "/" + str(i) + ".zip")
        zf.extractall(loc + "/" + str(i))
        os.remove(i)
        # Delete 201503.zip


# Step 4: Unzip the 2nd .zip files that were originally in the 1st .zip file (Ex: ANONYMOUS_DATA_201504_60453.csv.zip). Delete original .zip directory when done.
def unzpb():
    os.chdir(loc)
    for i in os.listdir():
        zf = ZipFile(loc + "/" + str(i) + "/" + str(i) + ".zip")
        zf.extractall(loc + "/" + str(i))
    dlt()

# Step 5: Delete all .csv.zip files
def dlt():
    os.chdir(loc)
    for i in os.listdir():
        j = os.chdir(loc + str(i))
        for j in os.listdir():
            if j[-4] == ".zip":
                os.remove(j)
    tbl()
# /tartarus/tylernass/201503abc

# Step 5: In progress

# def tbl():
#     conn = psycopg2.connect("dbname = smd user = tylernass password = test123")
#     sql_command = """CREATE TABLE smd (
#     ...
#     ...   Timestamp   TIMESTAMPTZ       NULL,
#     ...   Energy      DOUBLE PRECISION  NULL,
#     ...   Zipcode     INT               NULL,
#     ...   CustomerID  BIGINT               NULL
#     ... );"""
#     conn.execute(sql_command)
#     cvv()


# Step 6: Function used to create a table. Can be used anywhere.
def tbl():
    conn = psycopg2.connect("dbname = smd user = tylernass password = test123")
    sql_command = """CREATE TABLE smd (Timestampp TIMESTAMPTZ NULL, Energy DOUBLE PRECISION  NULL, Zipcode INT NULL, CustomerID BIGINT NULL);"""
    mycursor = conn.cursor()
    mycursor.execute(sql_command)
    cvv()
    # Open csv files
    # 12/02/12018 0030

# To be run in loc for every file
# Progress: Currently need to finish running and testing scripts
def cvv():
    vals = []
    for i in os.listdir():
        with open(i, 'r') as f:
            reader = csv.reader(f, delimiter = ',')
            firstline = True
            for row in reader:
                if firstline:
                    firstline = False
                    continue
                # Can I make this faster?
                zipcode = row[0] # if not use .strip()
                vals.append(zipcode)
                idd = row[3]
                vals.append(idd)
                d = datetime.strptime(row[4], '%m/%d/%Y')
                vals.append(d)
                for x in range(7, 54):
                    nrg = row[x]
                    vals.append(nrg)
            insrt(*vals)
            # Insrt(*vals) runs after every ROW in each FILE
# Date 03/31/2015
# Function used to connect to database


# Function used to migrate data from csv file to database. To be run in relevant location.
def insrt(*vals):
    # Vals[0:2] == Zipcode, ID, Date
    # Val[3:51] == NRG values for respective timestamps
    # Timestamp Energy Zipcode CustomerID
    timee = []
    sqql = "INSERT INTO smd(Timestampp, Energy, Zipcode, CustomerID) VALUES (%s, %s, %s, %s);"
    tme = 0
    for x in range(3, 50):
        if x % 2 == 0:
             tme = ((x-3))*50 + 50 # 4 == 0100 6 == 0200 8 == 0300
             one = tme /100
             two = 0
             timee.append(one)
             timee.append(two)
        if x % 2 == 1:
             tme = ((x-3))*50 + 30 # 3 == 0030 5 == 0130
             one = math.floor(tme/100)
             two = tme % 100
             timee.append(one)
             timee.append(two)


        tmm = time(timee[0], timee[1])
        timestmp = datetime.combine(vals[2], tmm)
        val = ((timestmp), vals[x], vals[0], vals[1])
        mycursor.execute(sqql, val)


