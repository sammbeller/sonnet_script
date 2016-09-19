#! /Library/Frameworks/Python.framework/Versions/3.5/bin/python3 

from bs4 import BeautifulSoup
import requests

URL='http://www.shakespeares-sonnets.com/sonnet/'
FAVORITES=[20,23,24,28,50]


f = open('sonnets.html', 'w')
for i in range(1, 151):
  r = requests.get(URL + str(i))
  data = r.text
  soup = BeautifulSoup(data, 'html.parser')
  sonnet = soup.find('div', {'id':'sonnet'})
  title = sonnet.find('h1')
  title['id'] = 'sonnet' + str(i)
  if i in FAVORITES:
    title['data-fav'] = 'true'
  f.write(str(title)
  f.write(str(sonnet.find('p', {'id': 'sonnettext'})).replace('\xa0', '&nbsp'))
