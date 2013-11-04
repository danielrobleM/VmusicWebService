
from iOStweet import iOStweet
import array
import os
from flask import Flask ,jsonify
import TwitterCore
app = Flask(__name__)
@app.before_request
@app.route('/')
def hello():
    return 'Hello World! 2'
tweet=TwitterCore.getTweet()
# print tweet
#create dict
x={}
for i in range (len(tweet)):
     Dict={
        'tweet_number  %s'%i:{'text':tweet[i]._tweetText,
        'Author':tweet[i]._Author}
        }
        
     # print Dict 
     x.update(Dict) 
     
# print jsonify(x)
print x
# print tweet[0]._tweetText
# print tweet[1]._tweetText
# A=json_myobj.iOStweet('ame','text','profile_image_url','retweet_count')
# A=json.loads(tweet)
# print A
@app.route('/api/v0.1/tasks', methods = ['GET'])
def get_tasks(): 
    return jsonify(x)

