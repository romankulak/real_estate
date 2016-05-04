# This file contains script to scrape the real-estate site and
#appends flats links to the rxt file

from bs4 import BeautifulSoup
import requests


url= requests.get("http://www.real-estate.lviv.ua/sale-kvartira/Lviv")
soup = BeautifulSoup(url.content)
all_search_divs = soup.find(id="search_result")
# all links in div 'search_result' :
links = all_search_divs.find_all("a")
#links = [ link.a for link in all_search_divs]
last_page = links [-1].get('href')

#get number after '_'
n = last_page.split('_')
last_page_number = n[1] # it is int type yet

s=[]
counter=0
for i in range(1, (int(last_page_number)+1)):
    cur_url = "http://www.real-estate.lviv.ua/sale-kvartira/Lviv/p_" + str(i)
    page = requests.get(cur_url)
    soup = BeautifulSoup(page.content)
    linkslist = soup.find_all("a", class_= "object-address")

    counter += 1
    print counter, "/", last_page_number

    for link in linkslist:
        s.append("http://www.real-estate.lviv.ua" + link.get("href"))

f = open('realtylinks.txt', 'w')
for url in s:
  print >> f, url
f.close()