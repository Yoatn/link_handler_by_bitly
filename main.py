import argparse
import os
import re
import requests
from dotenv import load_dotenv


def shorten_link(users_url_):
    headers = {
        'Authorization': f'Bearer {BITLY_TOKEN}',
        'Content-Type': 'application/json'
    }

    payload = {'long_url': users_url_,
               'DOMAIN': os.environ['DOMAIN'],
               'GROUP_GUID': os.environ['GROUP_GUID']
               }

    response = requests.post('https://api-ssl.bitly.com/v4/shorten',
                             headers=headers.copy(),
                             json=payload.copy())
    response.raise_for_status()
    bitlink = response.json()['link']
    return f'Битлинк {bitlink}'


def clicks_counter(short_url):
    headers = {
        'Authorization': f'Bearer {BITLY_TOKEN}',
        'Content-Type': 'application/json'
    }
    params = {
        'unit': 'day',
        'units': '-1'
    }

    short_url = re.sub('^https*:\/\/', '', short_url)
    response = requests.get(f'https://api-ssl.bitly.com/v4/bitlinks/'
                            f'{short_url}/clicks/summary',
                            headers=headers.copy(),
                            params=params.copy())
    response.raise_for_status()
    amount_clicks = response.json()['total_clicks']
    return 'По Вашей ссылке прошли ' + str(amount_clicks) + ' раз(а)'


def is_bitlink(url):
    headers = {
        'Authorization': f'Bearer {BITLY_TOKEN}',
    }
    url = re.sub('^https*:\/\/', '', url)
    response = requests.get(f'https://api-ssl.bitly.com/v4/bitlinks/{url}',
                            headers=headers)
    return response.ok


if __name__ == '__main__':
    load_dotenv()
    global BITLY_TOKEN
    BITLY_TOKEN = os.environ['BITLY_TOKEN']
    parser = argparse.ArgumentParser()
    parser.add_argument("users_url_arg")
    args = parser.parse_args()
    users_url = args.users_url_arg
    try:
        if is_bitlink(users_url):
            print(clicks_counter(users_url))
        else:
            print(shorten_link(users_url))
    except requests.exceptions.HTTPError:
        print(f'Invalid URL.')

