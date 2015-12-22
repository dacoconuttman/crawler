import csv
import HTMLParser

filename = '9d3dfb739fc3-list+of+urls.csv'
websites = []
with open(filename, 'r') as f:
    for line in f:
        websites.append(line)
        if 'str' in line:
            break
for site in websites:
    print site
