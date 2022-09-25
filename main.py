import requests
import pprint


def max_i(url):
    r = requests.get(url)
    name = ' '
    max_intelligence = 0
    for elem in r.json():
        if elem['name'] == 'Captain America' or elem['name'] == 'Hulk' or elem['name'] == 'Thanos':
            if elem["powerstats"]['intelligence'] > max_intelligence:
                max_intelligence = elem['powerstats']['intelligence']
                name = elem['name']
    return name


if __name__ == '__main__':
    print(max_i('https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json'))