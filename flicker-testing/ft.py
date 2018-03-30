inputfile = 'flicker-test-plan.md'

some_list = []

with open(inputfile, 'r') as f:
    for line in f:
        line = line.replace('[x]', '[ ]')
        line = line.replace('dev', 'staging')
        print line

        with open("newfile.md", "a") as myfile:
             myfile.write(line)

print 'All done'
