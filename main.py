import requests
from bs4 import BeautifulSoup

URL = 'http://www.liiofindia.org/in/cases/cen/INSC/1950/2.html'
headers = {'User-Agent': 'whatever'}

f = open("outputfile.txt", "w+")

page = requests.get(URL, headers= headers)

soup = BeautifulSoup(page.content, 'html.parser')

all_h2 = soup.find_all('h2', class_='make-database')
for h in all_h2:
    f.write(h.text)

all_p = soup.find_all('p')
for t in all_p:
    f.write(t.text)

f.close()