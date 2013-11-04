
from iOStweet import iOStweet
import array
import os
from flask import Flask ,jsonify
import TwitterCore
# from simplejson import simplejson as json
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World! 2'

tweet=TwitterCore.getTweet()
print tweet
#create dict
x={}
# A={
#    'text':tweet[0]._tweetText,
#     'Author':tweet[0]._Author
#     }
# x.update(A)
# C={
#     'text1':tweet[1]._tweetText,
#     'Author2':tweet[1]._Author
#     }
# x.update(C)
for i in range (len(tweet)):
     Dict={
        'tweet_number  %s'%i:{'text':tweet[i]._tweetText,
        'Author':tweet[i]._Author}
        }
        
     # print Dict 
     x.update(Dict) 
     

print x
print tweet[0]._tweetText
print tweet[1]._tweetText
orig = {
   'A': 1,
   'B': 2,
   'C': 3,
}

extra = {
   'D': 4,
   'E': 5,
}

# A=json_myobj.iOStweet('ame','text','profile_image_url','retweet_count')
# A=json.loads(tweet)
# print A
tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    }
]
@app.route('/api/v0.1/tasks', methods = ['GET'])
def get_tasks():
    # return jsonify( { 'tasks': tasks } 
    return jsonify(x)

