import requests
from bs4 import BeautifulSoup
import sys
import re

def scrapper(site):
    
    try:
        raw_site = requests.get(site)
        f = open("texty.txt", 'w')
        soup = BeautifulSoup(raw_site.content, 'lxml')
        heading = soup.find('h1')
        f.write(heading.text)
        f.write('\n')
        for item in soup.find_all('p')[1:]:
            text = item.text
            text = re.sub(' +',' ',text)
            f.write(text)
            f.write('\n')
        f.close()
        print('Finished')

    except requests.exceptions.RequestException as e:
        print('\n PROBLEM! \n', e)


if __name__ == "__main__":
    scrapper(sys.argv[1])
