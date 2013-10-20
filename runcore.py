import tweepy

 
# Consumer keys and access tokens, used for OAuth
consumer_key = 'UYDKjHxyhoszTHUcODlQg'
consumer_secret = 'pa4yTGSnSbgVpAQdeHNsL8SCUKfp7CH1xLDe7GxBA'

access_token = '351115984-n1VWKMf6rNXTWn6DHaYzHDYaPByn6YaIvTFDPqt6'
access_token_secret = 'iLzi261ZDGT2Hp0BkYQE0J4NDr6ALspV2A3KnwBM'
 
# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
 
# Creation of the actual interface, using authentication
api = tweepy.API(auth)

user = api.me()
 
print('Name: ' + user.name)
print('Location: ' + user.location)
print('Friends: ' + str(user.friends_count))