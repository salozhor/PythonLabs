from urllib.request import urlopen as op
from bs4 import BeautifulSoup as soup

url = "https://brokers.ru/grafik-foreks-online/aud-usd-kurs"
page = op(url)
data = page.read()
page.close()
soup1 = soup(data, "html.parser")
div = soup1.find('span', class_="tv-widget-chart__price-value.symbol-last")
print(data)