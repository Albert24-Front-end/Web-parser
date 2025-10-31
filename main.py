from openpyxl import Workbook
import requests
from bs4 import BeautifulSoup

workbook = Workbook()
worksheet = workbook.active

webpage = requests.get('https://live.skillbox.ru/playlists/code/python/')

soup = BeautifulSoup(webpage.text, 'html.parser')

items = soup.find_all(class_='playlist-inner__item')

for elem in items:
    title = elem.find(class_='playlist-inner-card__link-text').text
    relative_url = soup.find(class_='playlist-inner-card__link').attrs['href']
    full_url = f'https://live.skillbox.ru{relative_url}'
    row = [title, full_url]
    print(row)
    worksheet.append(row)

workbook.save('Free Skillbox webinars on Python.xlsx')

# abs_url = 'https://live.skillbox.ru' + relative_url

# print(soup.title.text)
