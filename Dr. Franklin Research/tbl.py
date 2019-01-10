def tbl():
    conn = psycopg2.connect("dbname = smd user = tylernass password = test123")
    sql_command = """CREATE TABLE Test(Energy DOUBLE PRECISION  NOT NULL, Zipcode INT NOT NULL, CustomerID BIGINT NOT NULL);"""
    mycursor = conn.cursor()
    mycursor.execute(sql_command)
    cvv()
