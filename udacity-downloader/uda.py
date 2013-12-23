#!/usr/bin/python
import urllib
import re
import sys
from bs4 import BeautifulSoup

reg = r'http.*zip"'
page = urllib.urlopen('https://www.udacity.com/wiki/st101/downloads').read()

soup = BeautifulSoup(page)

for i in re.findall(reg,page):
	print i[:-1]


#http://video.udacity-data.com/zip/st095/Orientation%21.zip