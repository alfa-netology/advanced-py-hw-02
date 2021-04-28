import json

class WikiCountryLink:

    def __init__(self, data_file_path):
        with open(data_file_path, encoding='utf-8') as file:
            data = json.load(file)

        self.WIKI_URL = "https://en.wikipedia.org/wiki/"
        self.countries_names_iter = iter(item.get('name').get('common') for item in data)

    def __iter__(self):
        return self

    def __next__(self):
        country_name = next(self.countries_names_iter)
        country_url = f'{self.WIKI_URL}{country_name.replace(" ", "_")}'
        return f"{country_name}, {country_url}"
