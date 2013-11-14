
from iOStweet import iOStweet
import array
import os
from flask import Flask ,jsonify
import TwitterCore
from flask import Response
import json
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World! 3'
tweets=TwitterCore.getTweet()
# print tweet
#create dict
x=[]
for tweet in tweets:
     # print Dict 
     a=dict({
        "text":tweet._tweetText,
        "author":tweet._Author})
     x.append(a) 
# print x
# print jsonify(x)

# print tweet[0]._tweetText
# print tweet[1]._tweetText
# A=json_myobj.iOStweet('ame','text','profile_image_url','retweet_count')
# A=json.loads(tweet)
# print A
@app.before_request
@app.route('/api/v0.1/tasks', methods = ['GET'])
def get_tasks():
	# rest = Response(x,status=200,mimetype='application/json')
	# rest.headers['Link']='http://127.0.0.1'
	# return json.loads(json.dumps(x,default=jdefault))
    # json.JSONEncoder.default(x)
    return json.dumps(x)
if __name__ == '__main__':
	app.run(debug=True )
