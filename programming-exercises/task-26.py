# Za pomocą webscrappera pobrać wszystkie oferty domów z podanego linku(https://www.otodom.pl/pl/wyniki/sprzedaz/mieszkanie/pomorskie/gdynia/gdynia/gdynia?priceMax=600000&viewType=listing), 
# każda oferta ma być obiektem klasy Home, który posiada atrybuty takie jak header_name, price, price_for_m2. 
# Wszystkie obiekty zapisać do słownika oraz do pliku home.csv.
import csv
import requests
from bs4 import BeautifulSoup

class Home:
    def __init__(self, header_name, price, price_for_m2):
        self.header_name = header_name
        self.price = price
        self.price_for_m2 = price_for_m2

def fetch_homes(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f"Error: {response.status_code}")
        return {}

    soup = BeautifulSoup(response.text, 'html.parser')
    print(soup.prettify())

    homes = {}
    listings = soup.find_all('article', {'data-cy': 'listing-item'})
    
    for listing in listings:
        header_name_tag = listing.find('p', {'data-cy': 'listing-item-title'})
        header_name = header_name_tag.text.strip() if header_name_tag else 'Brak tytułu'

        price_tag = listing.find('span', class_='css-2bt9f1 evk7nst0')
        price = price_tag.text.strip().replace('\xa0', ' ').replace('zł', '').strip() if price_tag else 'Brak ceny'

        price_for_m2_tag = listing.find('dt', string='Cena za metr kwadratowy')
        if price_for_m2_tag:
            price_for_m2_span = price_for_m2_tag.find_next('dd').find('span')
            price_for_m2 = price_for_m2_span.text.strip().replace('\xa0', '') if price_for_m2_span else 'Brak ceny za m2'
        else:
            price_for_m2 = 'Brak ceny za m2'

        home = Home(header_name, price, price_for_m2)
        homes[header_name] = home

    return homes

def save_homes_to_csv(homes, file_path):
    with open(file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['header_name', 'price', 'price_for_m2'])
        for home in homes.values():
            writer.writerow([home.header_name, home.price, home.price_for_m2])

    print(f"Dane zapisane do pliku {file_path}")

if __name__ == "__main__":
    url = 'https://www.otodom.pl/pl/wyniki/sprzedaz/mieszkanie/pomorskie/gdynia/gdynia/gdynia?priceMax=600000&viewType=listing'
    homes = fetch_homes(url)
    save_homes_to_csv(homes, 'home.csv')
