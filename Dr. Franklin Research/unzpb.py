def unzpb():
    os.chdir(loc)
    for i in os.listdir():
        zf = ZipFile(loc + "/" + str(i) + "/" + str(i) + ".zip")
        zf.extractall(loc + "/" + str(i))
    dlt()
