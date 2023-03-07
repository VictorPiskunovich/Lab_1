from bs4 import BeautifulSoup
import requests

def parse():
    f = open('file.txt', 'w', encoding='utf-8')
    url = 'https://omgtu.ru/general_information/faculties/'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")

    block = soup.find('div', id='pagecontent').find('ul').find_all('a')
    txt = ''
    for item in block:
        f.write(f"{item.text}\n")
        print(item.text)
parse()