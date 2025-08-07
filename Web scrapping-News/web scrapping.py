import requests
from bs4 import BeautifulSoup

url = "https://www.bbc.com/news"

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

headlines = soup.find_all('h3', class_='gs-c-promo-heading__title')

if not headlines:
    headlines = soup.find_all('h2')

with open('headlines.txt', 'w', encoding='utf-8') as f:
    for headline in headlines:
        text = headline.text.strip()
        f.write(text + '\n\n')

print("\nHeadlines have been saved to headlines.txt in the file Manager!")
