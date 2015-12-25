import csv
import HTMLParser
import Queue
import threading
# from bs4 import BeautifulSoup
import urllib
import urlparse
import mechanize

class Spider:

    def __init__(self, url):
        self.browser = mechanize.Browser()
        self.url = url
        self.toVisit = [url]
        self.visited = self.toVisit
    def crawl(self):
        while len(self.toVisit) > 0:
            try:
                self.browser.open(self.toVisit[0])
                self.toVisit.pop(0)
                for link in self.browser.links():
                    text = link.text().lower()
                    currUrl = link.url().lower()
                    if "financial" in text or "financial" in currUrl:
                        print link
                        return link.url()
                    else:
                        newurl = urlparse.urljoin(link.base_url, link.url)
                        if newurl not in self.visited and url in newurl:
                            self.visited.append(newurl)
                            self.toVisit.append(newurl)
                            print newurl
            except:
                print "Error"
                self.toVisit.pop(0)

def findPages(url, file):

    s = Spider(url)
    result = s.crawl()
    lock = threading.Lock()
    lock.acquire()
    try:
        file.write(result)
        file.write('\n')
    finally:
        lock.release()

websites = []

filename = '9d3dfb739fc3-list+of+urls.csv'
with open(filename, 'r') as file:
    for line in file.readlines():
        websites +=  line.strip().split('\r')

threads = []

outfile = open("results.txt", 'w')

for i in range(len(websites)):
    t = threading.Thread(target=findPages, args=(websites[i],outfile))
    threads.append(t)
    t.start()
