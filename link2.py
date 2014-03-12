#!/usr/bin/python
import sys
import urllib2
import bs4

request = urllib2.Request(sys.argv[1])
response = urllib2.urlopen(request)
soup = bs4.BeautifulSoup(response)
for link in soup.findAll('a'):
    print 'wget -c ' + sys.argv[1] + link.get('href')
