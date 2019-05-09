import requests


def shorten_url(url):
    site = 'https://chogoon.com/srt/api/'
    data = {'url': url}
    r = requests.post(url=site, data=data)
    return r.json()['data']['url']
