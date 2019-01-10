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
    sqlval = []
    timee = [0, 0, 0, 30, 1, 0, 1, 30, 2, 0, 2, 30, 3, 0, 3, 30, 4, 0, 4, 30, 5, 0, 5, 30, 6, 0, 6, 30, 7, 0, 7, 30, 8,
             0, 8, 30,
             9, 0, 9, 30, 10, 0, 10, 30, 11, 0, 11, 30, 12, 0, 12, 30, 13, 0, 13, 30, 14, 0, 14, 30, 15, 0, 15, 30, 16,
             0,
             16, 30, 17, 0, 17, 30, 18, 0, 18, 30, 19, 0, 19, 30, 20, 0, 20, 30, 21, 0, 21, 30, 22, 0, 22, 30, 23, 0,
             23,
             30]

    for x in range(0, 96, 2):
        # a = timee[x]
        # b = timee[x + 1]
        # t = time(a, b)
        # date = vals[2]
        # timestmp = datetime.combine(date, t).strftime('%m/%d/%Y %H:%M:%S')

        if x == 0:
            y = 3
        else:
            y = int(x/2 + 3)

        val = (vals[y], vals[0], vals[1])
        sqlval.append(val)

    sqql = "INSERT INTO EnergyUsage(Energy, Zipcode, CustomerID) VALUES(%s);"

    # for x in range(0, len(sqlval)):
    #     if x == (len(sqlval)-1):
    #         y = "(%s, %s, %s, %s)"
    #     else:
    #         y = "(%s, %s, %s, %s), "
    #
    #     sqql = sqql + y
    try:
        mycursor.executemany(sqql, sqlval)
        if(mycursor.executemany(sqql, sqlval)):
            print('Statement Executed')
            conn.commit()
    except:
        conn.rollback()

cvv()
# python /tartarus/tylernass/sqlinsrt.py
# conn.close()
# scp -r sqlinsrt.py tylernass@chaos.cs.uchicago.edu:/tartarus/tylernass
# scp tylernass@chaos.cs.uchicago.edu:/Users/tylernass/Desktop/energy-research/Chaos-Scripts/sqlinsrt.py tart
#
# def prnt():
# ...     conn = psycopg2.connect("dbname = smd user = tylernass password = test123")
# ...     mycursor = conn.cursor()
# ...     records = mycursor.fetchall()
# ...     for row in records:
# ...             print(row)




#### NEW EXAMPLE ####

# import psycopg2
# import config
#
#
# def insert_vendor_list():
#     vendor_list = [
#     ('AKM Semiconductor Inc.',),
#     ('Asahi Glass Co Ltd.',),
#     ('Daikin Industries Ltd.',),
#     ('Dynacast International Inc.',),
#     ('Foster Electric Co. Ltd.',),
#     ('Murata Manufacturing Co. Ltd.',)]
#
#     conn = psycopg2.connect("dbname = smd user = tylernass password = test123")
#     sql_command = """CREATE TABLE abc(vendor_name text NOT NULL);"""
#     cur = conn.cursor()
#     cur.execute(sql_command)
#     sql = "INSERT INTO abc(vendor_name) VALUES(%s)"
#     try:
#         # execute the INSERT statement
#         cur.executemany(sql,vendor_list)
#         # commit the changes to the database
#         conn.commit()
#         # close communication with the database
#         cur.close()
#     except (Exception, psycopg2.DatabaseError) as error:
#         print(error)
#     finally:
#         if conn is not None:
#             conn.close()
#
#

insert_vendor_list()
