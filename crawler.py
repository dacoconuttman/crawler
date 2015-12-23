import csv
import HTMLParser
import Queue
import threading

def findPages(url):
    print url
    return

def getWebsites(filename):
    websites = []
    with open(filename, 'r') as f:
        for line in f:
            print line
            websites.append(line)
            if 'str' in line:
                break
    return websites

siteList = getWebsites('9d3dfb739fc3-list+of+urls.csv')

threads = []

print len(siteList)

for site in range(len(siteList)):
    t = threading.Thread(target=findPages, args=(site,))
    threads.append(t)
    t.start()
