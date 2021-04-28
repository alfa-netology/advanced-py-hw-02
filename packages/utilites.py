import os
import hashlib

def makedir(path):
    if os.path.exists(path) is False:
        os.mkdir(path)

def generate_md5_hash(path):
    with open(path, encoding="utf-8") as file:
        for line in file:
            yield f"{line}MD5 hash: {hashlib.md5(line.encode()).hexdigest()}\n"

def get_wiki_links(path, data):
    print('Get & save wiki links for countries.')
    with open(path, 'w', encoding='utf-8') as links_file:
        for value in data:
            links_file.write(f'{value}\n')

def get_md5_hash(save_path, source_path):
    print('Get & save MD5 hash.')
    with open(save_path, 'w', encoding='utf-8') as md5_file:
        for hash_string in generate_md5_hash(source_path):
            md5_file.write(f"{hash_string}\n")
