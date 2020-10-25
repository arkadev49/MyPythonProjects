from requests import get
from bs4 import BeautifulSoup
from sys import argv

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/70.0.3538.77 Safari/537.36"}


def Translate(source, dest, word):
    url = 'https://context.reverso.net/translation/{}-{}/{}'.format(source, dest, word)

    r = get(url, headers=headers)
    if r:
        soup = BeautifulSoup(r.content, 'html.parser')
        res = soup.find('div', {'id': 'translations-content'})
        with open('{}.txt'.format(word), 'a', encoding='utf-8') as f:
            try:
                print('{} Translations:'.format(dest.capitalize()))
                f.write('{} Translations:\n'.format(dest.capitalize()))
                mean_d = res.text.split('  ')[5].strip()
                print(mean_d)
                f.write('{}\n'.format(mean_d))
                res = soup.find('div', {'class': 'example'})
                print('\n{} Examples:'.format(dest.capitalize()))
                f.write('\n{} Examples:\n'.format(dest.capitalize()))
                ex_s = res.text.split('  ')[5].strip()
                ex_d = res.text.split('  ')[10].strip()
                print('{}\n{}\n'.format(ex_s, ex_d))
                f.write('{}\n{}\n\n'.format(ex_s, ex_d))
            except:
                print('Something wrong with your internet connection')
                exit(0)
    else:
        print('Sorry, unable to find {}'.format(word))
        exit(0)


# print("Hello, you're welcome to the translator. Translator supports:")
#
lang_dict = {1: 'arabic',
             2: 'german',
             3: 'english',
             4: 'spanish',
             5: 'french',
             6: 'hebrew',
             7: 'japanese',
             8: 'dutch',
             9: 'polish',
             10: 'portuguese',
             11: 'romanian',
             12: 'russian',
             13: 'turkish'}

# for k, v in lang_dict.items():
#     print('{}. {}'.format(k, v.capitalize()))

# print('Type the number of your language:')
f_lang = argv[1]
# print("Type the number of a language you want to translate to or '0' to translate to all languages:")
t_lang = argv[2]
# print('Type the word you want to translate:')
trans = argv[3]
# print()

list_of_languages = [v for k, v in lang_dict.items()] + ['all']
if f_lang not in list_of_languages:
    print("Sorry, the program doesn't support", f_lang)
    exit(0)
if t_lang not in list_of_languages:
    print("Sorry, the program doesn't support", t_lang)
    exit(0)

with open('{}.txt'.format(trans), 'w', encoding='utf-8'):
    pass

if t_lang != 'all':
    Translate(f_lang, t_lang, trans)
else:
    for lang_no in range(1, 14):
        if f_lang != lang_dict[lang_no]:
            Translate(f_lang, lang_dict[lang_no], trans)
