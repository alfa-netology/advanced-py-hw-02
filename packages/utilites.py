import os

def makedir(path):
    if os.path.exists(path) is False:
        os.mkdir(path)

def get_countries_wiki_links(path, data):
    print('Get & save wiki links for countries')
    with open(path, 'w', encoding='utf-8') as links_file:
        for value in data:
            links_file.write(f'{value}\n')
