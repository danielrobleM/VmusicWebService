from twython import Twython

APP_KEY ='UYDKjHxyhoszTHUcODlQg'
APP_SECRET ='pa4yTGSnSbgVpAQdeHNsL8SCUKfp7CH1xLDe7GxBA'

OAUTH_TOKEN        = '351115984-n1VWKMf6rNXTWn6DHaYzHDYaPByn6YaIvTFDPqt6'
OAUTH_TOKEN_SECRET = 'iLzi261ZDGT2Hp0BkYQE0J4NDr6ALspV2A3KnwBM'

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
#twitter.verify_credentials()

import json 


search=json.dumps(twitter.search(q='iOSVmusic', rpp="50"))
search=json.loads(search)
cant_canciones=0
list_canciones= []
for entry in search['statuses']:
	list_canciones.append(str(entry['text']))
	cant_canciones=cant_canciones+1
print 'Cantidad de canciones= ',cant_canciones
print list_canciones

lhs, rhs = "2.7.0_bf4fda703454".split("_", 1)