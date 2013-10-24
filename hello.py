
from iOStweet import iOStweet
import os
from flask import Flask ,jsonify
import TwitterCore
# from simplejson import simplejson as json
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World! 2'

tweet=TwitterCore.getTweet()
print tweet[0]._Author
print tweet[1]._Author
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
@app.route('/API/V0.1/tasks', methods = ['GET'])
def get_tasks():
    return jsonify( { 'tasks': tweet } )
