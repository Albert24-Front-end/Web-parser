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
    relative_url = elem.find(class_='playlist-inner-card__link').attrs['href']
    abs_url = f'https://live.skillbox.ru{relative_url}'
    duration = elem.find(class_='playlist-inner-card__small-info').text.strip().split(',')[-1].strip()
    row = [title, abs_url, duration]
    print(row)
    worksheet.append(row)

workbook.save('Free Skillbox webinars on Python.xlsx')

# abs_url = 'https://live.skillbox.ru' + relative_url

# print(soup.title.text)
# Link to the presentation on this lesson:
# https://docs.google.com/presentation/d/1O2POeEA6fcRRONHDuez9QyMbW07kZ5yXgOZXB_WfIv0/edit?slide=id.g2161f0e6e8b_0_195#slide=id.g2161f0e6e8b_0_195
