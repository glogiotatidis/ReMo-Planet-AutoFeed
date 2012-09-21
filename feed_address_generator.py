#!/usr/bin/env python

import httplib
import json

def estb_conn():
    conn = httplib.HTTPSConnection('reps.mozilla.org')
    conn.request('GET', '/api/v1/rep/?format=json&limit=0')
    response = conn.getresponse()
    if response.status != 200:
        print 'Error : ', response.status, response.reason
    else:
        return (conn, response)

def filter_json(data):
    j_data = json.loads(data)
    for i in j_data['objects']:
        feed = i['profile']['personal_blog_feed'].strip()
        if feed:
            print '[%s]' % feed
            print 'name = %s' % i['fullname']
            print 'avatar = %s' % i['profile']['avatar_url']
            print ''

conn, response = estb_conn()
data = response.read()
filter_json(data)
conn.close()
