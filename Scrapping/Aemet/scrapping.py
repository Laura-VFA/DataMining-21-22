import requests
import os
from bs4 import BeautifulSoup

reqRoot = requests.get('https://datosclima.es/Aemet2013/DescargaDatos.html')
bsRoot = BeautifulSoup(reqRoot.content, 'html.parser')
tables = bsRoot.find('div', {"class": "story"}).find_all('table')

for table in tables:
    year = table.find('td').text.split(' ')[1]
    links = table.find_all('a')
    for link in links:
        print(f'{year}/{link.text}')
        reqRar = requests.get(f"https://datosclima.es/{link['href']}")
        reqRar.raw.decode_content = True
        os.makedirs(f'{year}/{link.text}')
        with open(f'{year}/{link.text}/{link.text}.rar', 'wb') as handler:
            handler.write(reqRar.content)
