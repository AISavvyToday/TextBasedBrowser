import argparse
import os
import requests
from bs4 import BeautifulSoup
from colorama import Fore, Back, Style


parser = argparse.ArgumentParser(description="Create a directory to store the webpage files")
parser.add_argument('dir', type=str, help="Directory name")
args = parser.parse_args()

try:
    if not os.path.exists(args.dir):
        os.mkdir(args.dir)
except FileExistsError:
    pass


def save_page(dir):
    with open(str(dir) + '/bloomberg.txt', 'w+') as bloom:
        bloom.write(response)
    with open(str(dir) + '/bloomberg.txt', 'r') as bloom:
        lines = bloom.readlines()
        for line in lines:
            print(line)


def get_page(page_url):
    r = requests.get(page_url)
    soup = BeautifulSoup(r.content, 'html.parser')
    content = Fore.BLUE + soup.get_text()
    return content


saved_tabs = []
while True:
    url = input('Enter webpage url: ')
    if '.' in url:
        if 'https://' in  url:
            response = get_page(url)
            save_page(args.dir)
            saved_tabs.append(response)
        else:
            url = 'https://' + url
            response = get_page(url)
            save_page(args.dir)
            saved_tabs.append(response)

    else:
        if url == 'exit':
            break
        elif url == 'bloomberg':
            url = 'https://' + url + '.com'
            response = get_page(url)
            save_page(args.dir)
            saved_tabs.append(response)
        elif url == 'nytimes':
            url = 'https://' + url + '.com'
            response = get_page(url)
            save_page(args.dir)
            saved_tabs.append(response)
        elif url == 'back':
            saved_tabs.pop()
            print(saved_tabs[-1])
        else:
            print('error, invalid url!')
