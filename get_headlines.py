# Script name    : get_headlines.py
# Author         : Abhishek kadian
# Created        : April 8, 2016
# Last Modified  : 
# Version        : 1.0


# Description: download news headlines from yahoo finance! The headlines|links are used to scrape news articles

import requests
import re
import io
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


companyname = raw_input("enter the company name : ")

searchurl = 'http://finance.yahoo.com/q?s='+companyname

#use fake useragent

ua = UserAgent();

head = ua.firefox.encode('ascii','ignore')
headers = {'useragent':head}

response = requests.get(searchurl, headers = headers)

content  = response.content

#parse
soup = BeautifulSoup(content,'html.parser')
links = soup.select('div.yfi_quote_headline ul > li > a')

print "search successful"
print "printing the search results in file"

with io.open('links.txt',encoding='utf-8', mode='w+') as ns:
	for link in links:
		ns.write(link.get('href')+'\n')

