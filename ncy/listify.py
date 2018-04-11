inputfile = 'qalinks.txt'

uuids = []

with open(inputfile, 'r') as f:
    for line in f:
        line = line.strip()
        uuid = line[29:]
        uuids.append(uuid)


print uuids
print '\n' + str(len(uuids)) + ' items'
