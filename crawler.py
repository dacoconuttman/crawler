import csv
import HTMLParser
import Queue
import threading

def findPages(url):
    t = threading.currentThread()
    print t
    print url
    return

websites = []

filename = '9d3dfb739fc3-list+of+urls.csv'
with open(filename, 'r') as file:
    for line in file.readlines():
        websites +=  line.strip().split('\r')

threads = []

for i in range(len(websites)):
    t = threading.Thread(target=findPages, args=(websites[i],))
    threads.append(t)
    t.start()
