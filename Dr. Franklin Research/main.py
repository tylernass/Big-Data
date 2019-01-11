# Starting location: /tartarus/DATASETS/SmartMeterData
orig = "/tartarus/DATASETS/SmartMeterData"
loc = "/tartarus/tylernass"

import os, zipfile
import shutil
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
    conn = psycopg2.connect("dbname = smd user = *** password = ***")
    sql_command = """CREATE TABLE Test(Energy DOUBLE PRECISION  NOT NULL, Zipcode INT NOT NULL, CustomerID BIGINT NOT NULL);"""
    mycursor = conn.cursor()
    mycursor.execute(sql_command)
    cvv()
    # Open csv files
    # 12/02/12018 0030

sqlval=[]
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
                zipcode = row[0] # if not use .strip()
                vals.append(zipcode)
                idd = row[3]
                vals.append(idd)
                if row[4] == 'DELIVERY CLASS PASSED':
                    continue
                else:
                    d = datetime.strptime(row[4], '%m/%d/%Y')
                    vals.append(d)
                for x in range(7, 55):
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
    timee = [0, 0, 0, 30, 1, 0, 1, 30, 2, 0, 2, 30, 3, 0, 3, 30, 4, 0, 4, 30, 5, 0, 5, 30, 6, 0, 6, 30, 7, 0, 7, 30, 8,
             0, 8, 30,
             9, 0, 9, 30, 10, 0, 10, 30, 11, 0, 11, 30, 12, 0, 12, 30, 13, 0, 13, 30, 14, 0, 14, 30, 15, 0, 15, 30, 16,
             0,
             16, 30, 17, 0, 17, 30, 18, 0, 18, 30, 19, 0, 19, 30, 20, 0, 20, 30, 21, 0, 21, 30, 22, 0, 22, 30, 23, 0,
             23,
             30]

    for x in range(0, 96, 2):
        a = timee[x]
        b = timee[x + 1]
        t = time(a, b)
        date = vals[2]
        timestmp = datetime.combine(date, t).strftime('%m/%d/%Y %H:%M:%S')

        if x == 0:
            y = 3
        else:
            y = int(x/2 + 3)

        val = (timestmp, vals[y], vals[0], vals[1])
        sqlval.append(val)

    sqql = ("INSERT INTO EnergyUsage(Timestampp, Energy, Zipcode, CustomerID) VALUES (%s, %s, %s, %s)")

    # for x in range(0, len(sqlval)):
    #     if x == (len(sqlval)-1):
    #         y = "(%s, %s, %s, %s)"
    #     else:
    #         y = "(%s, %s, %s, %s), "
    #
    #     sqql = sqql + y
    try:
        mycursor.executemany(sqql, sqlval)
    except:
        conn.rollback()

def cnct():
    conn = psycopg2.connect("dbname = smd user = *** password = ***")
    mycursor = conn.cursor()
