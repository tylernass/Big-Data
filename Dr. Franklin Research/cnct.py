def cnct():
    conn = psycopg2.connect("dbname = smd user = tylernass password = test123")
    mycursor = conn.cursor()
