from bs4 import BeautifulSoup
import requests

url = 'https://www.flipkart.com/search?q=shoes&otracker=search&otracker1=search&otracker2'
page = requests.get(url)
if not page.status_code == 200:
    print('An error has occured.')
    exit()
soup = BeautifulSoup(page.text, 'html5lib')

items = soup.find_all('div', class_='_2B099V')
for item in items:
    name = item.find('a').text
    price = item.find('div', class_='_30jeq3').text
    print(name, price)