#!/usr/bin/python
"""
some docstring here
"""
import requests
#import urllib
#from bs4 import BeautifulSoup



inputfile = 'nestedterms.txt'

urls = []
with open(inputfile, 'r') as f:
    for line in f:
        url = line[0:69]
        #print url
        urls.append(url)

# print urls

broken_links = []
for u in urls:
    r = requests.get(u)
    status = r.status_code
    if r.ok:
        print (u + ': OK')
    else:
        print ('Error code ' + str(status) + ' found on: ' + u)
        broken_links.append(u)

print('Number of broken links: ' + str(len(broken_links)))

if len(broken_links) > 0:
    print('List of broken links: ')
    for b in broken_links:
        print ('\t' + b)


# REFERENCE TO BE DELETED BELOW
#def choose_file():
#    file_name = raw_input("Enter the name of your text input file " +
#                           "(default is 'nestedterms.txt'): ")
#     return file_name if bool(file_name) else 'input.txt'

# address = 'http://oscms-qa.openstax.org/sitemap.xml'
# xml = urllib.urlopen(address).read()

# print ("Retrieving sitemap from " + address + ", processing...")

# soup = BeautifulSoup(xml, 'lxml')

# links = []
# qalinks = []
#
# # gather all the links from the sitemap.xml into a list
# for s in soup.find_all('loc'):
#     links.append(s.text)
#
# # rewrite those links to use the QA domain and put into another list
# for link in links:
#     newlink = link.replace('openstax.org', 'oscms-qa.openstax.org')
#     qalinks.append(newlink)
#
# broken_links = []
# for link in qalinks:
#     r = requests.get(link)
#     status = r.status_code
#     if r.ok:
#         print (link + ': OK')
#     else:
#         print ('Error code ' + str(status) + ' found on: ' + link)
#         broken_links.append(link)
#
# print('Number of broken links: ' + str(len(broken_links)))
#
# if len(broken_links) > 0:
#     print('List of broken links: ')
#     for link in broken_links:
#         print ('\t' + link)
