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
                print(d)
                vals.append(d)

                for x in range(7, 54):
                    nrg = row[x]
                    vals.append(nrg)
            insrt(*vals)
