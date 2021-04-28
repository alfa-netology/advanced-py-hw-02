from packages.classes import WikiCountryLink
from packages import utilites

data = WikiCountryLink('data/countries.json')

utilites.makedir('output/')

links_file = 'output/countries_wiki_links.txt'
utilites.get_countries_wiki_links(links_file, data)
