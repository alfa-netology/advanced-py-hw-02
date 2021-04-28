from packages.classes import WikiCountryLink
from packages import utilites

data = WikiCountryLink('data/countries.json')

utilites.makedir('output/')

links_file = 'output/countries_wiki_links.txt'
utilites.get_countries_wiki_links(links_file, data)

md5_hash_file = 'output/countries_wiki_md5.txt'
utilites.get_countries_md5_hash(md5_hash_file, links_file)