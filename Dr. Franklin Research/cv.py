sqlval = []
def cvv():
    for i in os.listdir():
        vals = []
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
                if row[4] == 'DELIVERY CLASS PASSED':
                    continue
                else:
                    # d = datetime.strptime(row[4], '%m/%d/%Y')
                    d = parse(row[4])
                    vals.append(d)
                for x in range(7, 55):
                    nrg = row[x]
                    vals.append(nrg)
                insrt(*vals)
