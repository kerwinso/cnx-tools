#!/usr/bin/python
"""
some docstring here
"""

# Read the file, change URLs to qa domain
inputfile = 'nestedterms.txt'
urls = {}
with open(inputfile, 'r') as f:
    for line in f:
        url = line[0:69]
        url_title = line[72:].strip()
        new_link = url.replace('staging', 'qa')
        urls[new_link] = url_title

print urls

# create an ordered HTML file with links to all the things
with open("qa-urls-new.html", "a") as myfile:
    for new_link, url_title in urls.items():
        myfile.write('<li><a href="' + new_link + '">' + new_link + '</a> ' + url_title + '</li>\n')


## Check for broken links on qa
# import requests
# broken_links = []
# print "Checking http status codes..."
# for u in urls:
#     r = requests.get(u)
#     status = r.status_code
#     if r.ok:
#         pass
#         # print (u + ': OK')
#     else:
#         print ('Error code ' + str(status) + ' found on: ' + u)
#         broken_links.append(u)
#
# print('Number of broken links: ' + str(len(broken_links)))
#
# if len(broken_links) > 0:
#     print('List of broken links: ')
#     for b in broken_links:
#         print ('\t' + b)


## Aborted attempts to automate capturing the data/content/screenshots of all the URLs for diffing later
# import urllib
# for u in urls:
#     #print u
#     short_id = u[28:36]
#
#     # Read content of each URL, write to a file: FAIL, doesn't load page content
#     # page = urllib.urlopen(u)
#     # f = open("./data/" + short_id + ".txt", "w")
#     # content = page.read()
#     # f.write(content)
#     # f.close()
#     # # print(content)
#
#     # Try taking a screenshot in selenium instead: FAIL, doesn't grab the whole page
#     from selenium import webdriver
#     from selenium.webdriver.common.by import By
#     from selenium.webdriver.support.ui import WebDriverWait
#     from selenium.webdriver.support import expected_conditions as EC
#     print "launching browser for " + u
#     driver = webdriver.Chrome()
#     wait = WebDriverWait(driver, 10)
#
#     driver.get(u)
#
#     # wait until Metadata tab in footer is found
#     try:
#         element = WebDriverWait(driver, 10).until(
#             EC.presence_of_element_located((By.ID, "metadata-tab"))
#         )
#         driver.save_screenshot('./screenshots/' + short_id + '.png')
#     except:
#         print "Element not found :("
#     finally:
#         driver.quit()
#

