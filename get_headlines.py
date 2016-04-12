'''Script name : get_headlines.py
Author         : Abhishek kadian
Created        : April 8, 2016
Last Modified  : April 12,2016
Version        : 1.0'''


'''Description: download news headlines from yahoo finance!
The headlines|links are used to scrape news articles'''

import requests
import io
import time
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


companyName = raw_input("enter the Stock name : ")

def gethealine(companyName, day):
    "get the headlines"
    date = '2016-02-'+str(day)
    searchUrl = 'http://finance.yahoo.com/q/h?s='+companyName+'&t='+date
    #use fake useragent
    ua = UserAgent();
    head = ua.firefox.encode('ascii', 'ignore')
    headers = {'useragent':head}
    response = requests.get(searchUrl, headers=headers)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    links = soup.select('div.yfi_quote_headline ul > li > a')

    '''write the search results in file, a new file for each day'''
    
    filename = 'links'+str(day)+'.txt'
    with io.open(filename, encoding='utf-8', mode='w+') as ns:
        for link in links:
	        ns.write(link.get('href')+'\n')
        ns.close()


#run the loop for 29 days: Month of Feburary
day = 29
while day > 0:
    gethealine(companyName, day)
    time.sleep(5)
    day = day-1

print "Successful. All headlines have been saved to disk"
