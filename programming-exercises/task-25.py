# Za pomocą pakietu do web-scrappingu, np.beautifulsoup lub jsoup, zapisać do tablicy wszystkie hiperłącza występujące na wybranej przez siebie stronie.
import requests
from bs4 import BeautifulSoup  

url = 'https://en.wikipedia.org/wiki/Web_scraping'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

links = []
for a in soup.find_all('a', href=True):
    links.append(a['href'])

with open('links.txt', 'w') as file:
    for link in links:
        file.write(link + '\n')