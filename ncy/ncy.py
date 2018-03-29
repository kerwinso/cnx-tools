#!/usr/local/bin/python
"""
look for a string in each of a list of URLs in a text doc
"""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

inputfile = 'qalinks.txt'
urls_with_ncy = []

driver = webdriver.Chrome()
driver.set_window_position(720, 0)  # fullscreen:1280|laptop:720
driver.set_window_size(720, 800)  # fullscreen:1280,1000|laptop:720,800
driver.execute_script('window.focus()')

with open(inputfile, 'r') as f:
    print 'Reading URLs from:', inputfile
    for line in f:
        try:
            line = line.strip()
            print 'Opening url in Chrome:', line
            wait = WebDriverWait(driver, 5)
            driver.get(line)
            print 'Looking for NOT_CONVERTED_YET...'
            ncy = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'not-converted-yet')))
            if ncy:
                print 'NCY found! Element text:', ncy.text
                urls_with_ncy.append(line)
        except:
            print 'Not found, moving on.'

driver.quit()
print '\n Total NCY found: ', len(urls_with_ncy)

if len(urls_with_ncy) > 0:
    print ('These pages still show NOT_CONVERTED_YET: ')
    for url in urls_with_ncy:
        print (url)
