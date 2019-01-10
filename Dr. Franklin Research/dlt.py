def dlt():
    os.chdir(loc)
    for i in os.listdir():
        j = os.chdir(loc + str(i))
        for j in os.listdir():
            if j[-4] == ".zip":
                os.remove(j)
    tbl()
