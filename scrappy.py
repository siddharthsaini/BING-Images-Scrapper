import os
import json 
import requests
from bs4 import BeautifulSoup

usr_agent = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'none',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive',
}
    
def main():
    imageLinks = []

    data = input('What are you looking for? ')
    n_images = int(input('How many images do you want? '))
    height = input('Height for images? ')
    width = input('Width for images? ')

    print('Start searching...')
    
    searchurl = 'https://www.bing.com/images/search?&q='+ data +'&qft=+filterui:imagesize-custom_'+ width +'_'+ height +'&FORM=IRFLTR'
    print(searchurl)

    response = requests.get(searchurl, headers=usr_agent)
    html = response.text

    soup = BeautifulSoup(html, 'html.parser')
    links = soup.findAll('a', {'class': 'iusc'}, m=True, limit=n_images)

    for lin in links:
        parsed_json = lin['m']
        python_json = json.loads(parsed_json)
        img_link = python_json['murl']
        imageLinks.append(img_link)

    print(imageLinks)


if __name__ == '__main__':
    main()
