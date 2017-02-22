import requests
from bs4 import BeautifulSoup

url = 'http://www.nytimes.com'
r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html, "lxml")
soup.find('')

head_links = soup.findAll('h2',{'class':'story-heading'})

for n in head_links :
  a = n.find('a')
  print (a)
  #print n.get['href'] 


#print(soup.find('span', 'articletitle').string)
#titles = []
#titles.push(soup.find('span', 'articletitle').string)