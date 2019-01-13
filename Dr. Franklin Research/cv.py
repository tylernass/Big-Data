# To be run in loc for every file
# Progress: Currently need to finish running and testing scripts
sqlval = []
strt = 0
def cvv():
    for i in os.listdir():
        with open(i, 'r') as f:
            vals = []
            reader = csv.reader(f, delimiter = ',')
            firstline = True
            for row in reader:
                if firstline:
                    firstline = False
                    continue
                else:
                    zipcode = row[0] # if not use .strip()
                    vals.append(zipcode)
                    idd = row[3]
                    vals.append(idd)
                    if row[4] == 'DELIVERY CLASS PASSED':
                        continue
                    else:
                        # d = datetime.strptime(row[4], '%m/%d/%Y')
                        d = row[4]
                        vals.append(d)
                    for x in range(7, 55):
                        nrg = row[x]
                        vals.append(nrg)
                insrt(*vals)
                print('1. Done')
                vals.clear()
            # Insrt(*vals) runs after every ROW in each FILE
