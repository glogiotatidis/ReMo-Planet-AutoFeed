#!/usr/bin/env python
import requests

BASE_URL = 'https://reps.mozilla.org'
URL = '/api/v1/rep/?format=json&limit=20'


def main():
    entries = []
    new_url = URL
    while True:
        response = requests.get(BASE_URL + new_url, verify=False)
        if not response.status_code == 200:
            raise ValueError('Invalid Response')

        data = response.json()
        for item in data['objects']:
            feed = item['profile']['personal_blog_feed'].strip()
            if feed:
                entries.append({
                    'feed': feed,
                    'name': item['fullname'],
                    'avatar': item['profile']['avatar_url']
                    })

        new_url = data['meta'].get('next', None)
        if not new_url:
            break

    # Hardcoded official reps blog
    entries.append({
        'feed': 'https://blog.mozilla.org/mozillareps/feed/',
        'name': 'Official Reps Blog',
        'avatar': 'https://reps.mozilla.org/static/base/img/remo/remo_logo_medium.png',
    })

    for entry in entries:
        print '[%s]' % entry['feed']
        print 'name = %s' % entry['name']
        print 'avatar = %s' % entry['avatar']
        print ''


if __name__ == '__main__':
    main()
