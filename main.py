from packages.classes.wiki import WikiCountryLink


x = WikiCountryLink('data/countries.json')

for i in x:
    print(i)