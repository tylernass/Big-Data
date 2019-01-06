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
    timee = [0, 0, 0, 30, 1, 0, 1, 30, 2, 0, 2, 30, 3, 0, 3, 30, 4, 0, 4, 30, 5, 0, 5, 30, 6, 0, 6, 30, 7, 0, 7, 30, 8,
             0, 8, 30,
             9, 0, 9, 30, 10, 0, 10, 30, 11, 0, 11, 30, 12, 0, 12, 30, 13, 0, 13, 30, 14, 0, 14, 30, 15, 0, 15, 30, 16,
             0,
             16, 30, 17, 0, 17, 30, 18, 0, 18, 30, 19, 0, 19, 30, 20, 0, 20, 30, 21, 0, 21, 30, 22, 0, 22, 30, 23, 0,
             23,
             30]
    sqql = "INSERT INTO smd(Timestampp, Energy, Zipcode, CustomerID) VALUES (%s, %s, %s, %s);"


    for x in range(0, 96, 2):
        a = timee[x]
        b = timee[x + 1]
        t = time(a, b)
        date = datetime.strptime(vals[2], "%m/%d/%Y")
        timestmp = datetime.combine(date, t)
        if x == 0:
            y = 0
        else:
            y = x/2 + 3
        val = ((timestmp), vals[y], vals[0], vals[1])
        mycursor.execute(sqql, val)



def cnct():
    conn = psycopg2.connect("dbname = smd user = tylernass password = test123")
    mycursor = conn.cursor()
