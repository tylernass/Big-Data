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
    dtee = parse(vals[2])

    for x in range(0, 96, 2):
        a = timee[x]
        b = timee[x + 1]
        t = time(a, b)

        try:
            timestmp = datetime.combine(dtee, t).strftime('%Y-%m-%d %H:%M:%S')
        except:
            continue

        if x == 0:
            y = 3
        else:
            y = int(x/2 + 3)

        val = (timestmp, vals[y], vals[0], vals[1])
        sqlval.append(val)

    print('2. Done')
    sqql = ("INSERT INTO EnergyUsage(Timestampp, Energy, Zipcode, CustomerID) VALUES (%s, %s, %s, %s)")
    print('3. Done')
    # for x in range(0, len(sqlval)):
    #     if x == (len(sqlval)-1):
    #         y = "(%s, %s, %s, %s)"
    #     else:
    #         y = "(%s, %s, %s, %s), "
    #
    #     sqql = sqql + y
    try:
        mycursor.executemany(sqql, sqlval)
        sqlval.clear()
        x = timeit.default_timer() - strt
        print('Time to execute: ', x)
    except:
        conn.rollback()


cvv()
