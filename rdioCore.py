#!/usr/bin/env python
import oauth2 as oauth
import urllib
import json
consumer = oauth.Consumer('5masx9sysdbezm2m6gjrcher', 'NgnbvuBcCT')
client = oauth.Client(consumer)
#response = client.request('http://api.rdio.com/1/', 'POST', urllib.urlencode({'method': 'get', 'keys': 'a184236,a254895,a242205'}))
response = client.request('http://api.rdio.com/1/', 'POST', urllib.urlencode({'method': 'search','query': 'S&M','types': 'Track' }))
#print response[1]
#data_string = json.loads(response)
Jresponse = json.loads(response[1])
#print json.dumps(Jresponse, indent=4, sort_keys=True)
result= Jresponse['result']
#print json.dumps(result, indent=4, sort_keys=True)
print 'Album:',result['results'][0]['album']
print 'Artist:',result['results'][0]['artist']
print 'key:',result['results'][0]['key']
print 'Icon400:',result['results'][0]['icon400']
print 'Icon200:',result['results'][0]['icon']
