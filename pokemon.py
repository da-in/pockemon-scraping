from bs4 import BeautifulSoup
import re
import csv

File = open('./pokemon_site.html', encoding='utf=8').read()

with open('poketmon.csv', 'w', encoding="utf-8", newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['number', 'name', 'img_link', 'type1', 'type2'])

soup = BeautifulSoup(File, 'html.parser')

pokemon_list = soup.select('#pokedexlist > li')

with open('poketmon.csv', 'a', encoding="utf-8", newline='') as csv_file:
    csv_writer = csv.writer(csv_file)

    for item in pokemon_list:
        # number, name
        text = item.select_one('a > div.bx-txt > h3').getText().split()

        # img_link
        img_link = item.select_one('a > div.img > div > img')['src']
        img_link = re.sub(r'[^0-9]', '', img_link)
        img_link = f'https://data1.pokemonkorea.co.kr/newdata/pokedex/mid/{img_link}.png'

        # ptype
        type_list = item.select('a > div.bx-txt > span')
        try:
            type1 = type_list[0].getText()
        except IndexError as e :
            type1 = 'null'

        try:
            type2 = type_list[1].getText()
        except IndexError as e :
            type2 = 'null'
        
        # write csv
        csv_writer.writerow([text[0], text[1], img_link, type1, type2])