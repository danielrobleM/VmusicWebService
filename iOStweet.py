import json
class iOStweet (object):
	"""This class define a iOStweet """
	"""Twitter Elements"""
	_Retweet=None
	_Author=None
	_tweetText=None
	_ProfileImage=None
	"""Rdio Elements"""
	_Artist=None
	_Song=None
	_Album=None
	_Icon400=None
	_Icon200=None
	_Key=None

	def __init__(self,_Author,_tweetText,_ProfileImage,_Retweet):
		# super( , self).__init__()
		self._Author = _Author
		self._Retweet = _Retweet
		self._Song = None
		self._tweetText = _tweetText
		self._ProfileImage = _ProfileImage
		self._Artist = None
	def iOStweet(self):
		return self
	
