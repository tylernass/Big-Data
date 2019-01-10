def mkdr():
    for i in os.listdir():
        nm = i[:6]
        os.mkdir(loc + "/" + str(nm))
    mgt()
