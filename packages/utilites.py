import os
from hashlib import md5

def makedir(path):
    if os.path.exists(path) is False:
        os.mkdir(path)

def generate_hash(source_path):
    with open(source_path, encoding="utf-8") as file:
        for line in file:
            yield f"{line}MD5 hash: {md5(line.encode()).hexdigest()}\n"

def get_wiki_links(links_file, data):
    print('Get & save wiki links for countries.')
    with open(links_file, 'w', encoding='utf-8') as file:
        for value in data:
            file.write(f'{value}\n')

def get_hash(hash_file, source_path):
    print('Get & save MD5 hash.')
    with open(hash_file, 'w', encoding='utf-8') as file:
        for hash_string in generate_hash(source_path):
            file.write(f"{hash_string}\n")
