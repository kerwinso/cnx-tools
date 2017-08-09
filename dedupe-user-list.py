"""
Removes duplicates from a text list of users (one per line) and 
outputs list of unique users into another text file.
"""

users =[]

with open('users to copy from production.txt', 'r') as f:
	for line in f:
		line = line.rstrip()
		users.append(line)

unique_users = []

for user in users:
	if user in unique_users:
		continue
	else:
		unique_users.append(user)

print unique_users

for u in unique_users:		
	with open("unique_users.txt", "a") as t:
		t.write("{0} \n".format(u))

print "unique_users.txt file created."
