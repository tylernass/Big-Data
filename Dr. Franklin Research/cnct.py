def cnct():
    conn = psycopg2.connect("dbname = smd user = NA password = NA")
    mycursor = conn.cursor()
