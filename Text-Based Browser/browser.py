import os
from sys import argv
import requests as req
from bs4 import BeautifulSoup
import re
from colorama import Fore, Style, init

init(autoreset=True)

dirname = argv[1]
dir_path = os.getcwd() + '\\' + dirname


def get_contents(r_content):
    soup = BeautifulSoup(r_content, 'html.parser')
    new_content = ''
    for i in soup.stripped_strings:
        if re.search("[a-zA-Z0-9]+", i):
            new_content += i + '\n'
    links = soup.find_all('a')
    return new_content, links


def remove_ext(name):
    return name.replace('.', '')


def check_files(f_name):
    file_list = [_ for _ in os.listdir(dir_path)]
    for file in file_list:
        if f_name in file:
            return file
    return False


def read_file(f_name):
    with open('{}\\{}'.format(dir_path, remove_ext(f_name)), 'r', encoding='utf-8') as f:
        read_text = f.read()
    return read_text


def save(name, content):
    filename = remove_ext(name)

    try:
        with open('{}/{}'.format(dir_path, filename), 'w', encoding='utf-8') as file:
            file.write(content)
    except UnicodeEncodeError as error:
        print(error)


try:
    os.mkdir(dirname)
except OSError:
    pass

stk = []
prevPage = None

while True:
    choice = input()
    if choice != 'back' and prevPage is not None:
        if prevPage != 'back':
            stk.append(prevPage)
    if choice == 'exit':
        exit(0)
    elif check_files(choice):
        prevPage = read_file(check_files(choice))
        print(prevPage)
    elif choice == 'back':
        if stk:
            print(stk.pop())
    else:
        if not choice.startswith('https://'):
            url = 'https://' + choice
        else:
            url = choice
        # noinspection PyBroadException
        try:
            r = req.get(url)
            text_contents, link_contents = get_contents(r.content)
            write_content = text_contents
            text_contents = text_contents.split('\n')
            prevPage = ""
            for link in link_contents:
                for text in text_contents:
                    if link.text in text:
                        prevPage += text.replace(link.text, Fore.BLUE + link.text + Style.RESET_ALL) + '\n'
                        print(text.replace(link.text, Fore.BLUE + link.text + Style.RESET_ALL))
            print()
            save(choice, prevPage)
        except:
            print('Error: Incorrect URL\n')
