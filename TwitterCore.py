from twython import Twython
from iOStweet import iOStweet
def getTweet():
 APP_KEY ='UYDKjHxyhoszTHUcODlQg'
 APP_SECRET ='pa4yTGSnSbgVpAQdeHNsL8SCUKfp7CH1xLDe7GxBA'

 OAUTH_TOKEN        = '351115984-n1VWKMf6rNXTWn6DHaYzHDYaPByn6YaIvTFDPqt6'
 OAUTH_TOKEN_SECRET = 'iLzi261ZDGT2Hp0BkYQE0J4NDr6ALspV2A3KnwBM'

 twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
 #twitter.verify_credentials()

 import json 


 search=json.dumps(twitter.search(q='iOSVmusic', rpp="50"))
 search=json.loads(search)
 Cant_Song=0 #Cant_Song
 List_song= []#List_song
 for entry in search['statuses']:
	 # text= List_song.append(str(entry['text']))
	 # retweet_count= List_song.append(str(entry['retweet_count']))
	 # name=List_song.append(str(entry['user']['name']))
	 # profile_image_url=List_song.append(str(entry['user']['profile_image_url']))
      # tballbalb=str(entry['text'])
      text=entry['text']
      # call a function for know is text has the right format Author + song
      # if No , forget this node , else continue
      # call RdioCore For get Album,Artist,Key,Icons(200,400)
      retweet_count=entry['retweet_count']
      name=entry['user']['name']
      profile_image_url=entry['user']['profile_image_url']
      tweet=iOStweet(name,text,profile_image_url,retweet_count)
      # print tweet
      List_song.append(tweet)
      Cant_Song=Cant_Song+1
 print 'Cantidad de canciones= ',Cant_Song
 ##print List_song

 lhs, rhs = "2.7.0_bf4fda703454".split("_", 1)
 return List_song