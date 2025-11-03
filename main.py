import os
from datetime import datetime
from openpyxl import Workbook
from openpyxl.styles import Font, Alignment
import requests
from bs4 import BeautifulSoup

# Создаем папку для временных файлов
TEMP_DIR = 'temp_excel'
if not os.path.exists(TEMP_DIR):
    os.makedirs(TEMP_DIR)

# Создание нового excel файла
workbook = Workbook()
worksheet = workbook.active # Первый лист
# worksheet.title = 'Мои данные'  # Переименовать лист

# Жирные заголовки
headers = ['Название', 'Ссылка', 'Длительность']
worksheet.append(headers)
for cell in worksheet[1]:
    cell.font = Font(bold=True, size=12)
    cell.alignment = Alignment(horizontal='center', vertical='center')

# Парсинг
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

# Сохраняем название файла с датой и версией
date_str = datetime.now().strftime('%Y-%m-%d')
version = 1

while True:
    filename = os.path.join(TEMP_DIR, f'Free Skillbox webinars on Python {date_str} v{version}.xlsx')
    if not os.path.exists(filename):
        break
    version += 1

# Сохраняем excel файл
workbook.save(filename)

# abs_url = 'https://live.skillbox.ru' + relative_url

# print(soup.title.text)
# Link to the presentation on this lesson:
# https://docs.google.com/presentation/d/1O2POeEA6fcRRONHDuez9QyMbW07kZ5yXgOZXB_WfIv0/edit?slide=id.g2161f0e6e8b_0_195#slide=id.g2161f0e6e8b_0_195
