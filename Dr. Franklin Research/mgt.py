def mgt():
    for i in os.listdir():
        nw = (loc + "/" + str(i))
        cp = "/tartarus/DATASETS/SmartMeterData/" + str(i)
        shutil.copy2(cp, nw)
    unzpa()
