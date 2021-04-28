from packages.classes import WikiCountryLink
from packages import utilites

data = WikiCountryLink('data/countries.json')

utilites.makedir('output/')

links_file = 'output/links.txt'
utilites.get_wiki_links(links_file, data)

md5_hash_file = 'output/md5.txt'
utilites.get_md5_hash(md5_hash_file, links_file)
