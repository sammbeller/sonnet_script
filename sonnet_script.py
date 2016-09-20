#! /Library/Frameworks/Python.framework/Versions/3.5/bin/python3 

from bs4 import BeautifulSoup
import requests

URL='http://www.shakespeares-sonnets.com/sonnet/'
FAVORITES=[20,23,24,28,50,74]


# Set up new document
new_soup = BeautifulSoup('', 'html.parser')
index = new_soup.new_tag('<ul id="index"></ul>')
new_soup.insert(1, index)
favorites = new_soup.new_tag('<ul id="favorites"></ul>')
new_soup.insert(2, favorites)
current_el = favorites

f = open('sonnets.html', 'w')
f2 = open('soup_sonnets.html', 'w')
for i in range(1, 151):
  # grab the doc and convert
  r = requests.get(URL + str(i))
  data = r.text
  document = BeautifulSoup(data, 'html.parser')

  # Add to new document
  sonnet = document.find('div', {'id':'sonnet'})
  current_el.insert_after(sonnet)
  current_el = sonnet

  title = sonnet.find('h1')
  title['id'] = 'sonnet' + str(i)
  if i in FAVORITES:
    title['data-fav'] = 'true'

  f.write(str(title))
  f.write(str(sonnet.find('p', {'id': 'sonnettext'})).replace('\xa0', '&nbsp'))

f2.write(str(new_soup))
