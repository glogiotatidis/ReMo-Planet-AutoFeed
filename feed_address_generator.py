#!/usr/bin/env python
import requests

BASE_URL = 'https://reps.mozilla.org'
URL = '/api/v1/rep/?format=json&limit=20'

def main():
    new_url = URL
    while True:
        response = requests.get(BASE_URL + new_url, verify=False)
        if not response.status_code == 200:
            raise ValueError('Invalid Response')

        data = response.json()
        for item in data['objects']:
            feed = item['profile']['personal_blog_feed'].strip()
            if feed:
                print '[%s]' % feed
                print 'name = %s' % item['fullname']
                print 'avatar = %s' % item['profile']['avatar_url']
                print ''

        new_url = data['meta'].get('next', None)
        if not new_url:
            break


if __name__ == '__main__':
    main()
