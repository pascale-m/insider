from twython import Twython
from watson_developer_cloud import PersonalityInsightsV3
import time
import sys
import json
import codecs
from klout import *


CONSUMER_KEY = 'GdVE1KUrR9A3Cj3OodaGARFaw'
CONSUMER_SECRET = 'XgLJvHMFP5EbnZxJDs9o92nTILyDgCwSK21e3zrfRNb4spO32t'
ACCESS_KEY = '740727093382643713-DtNLbAyqa2CGKhGcdGOsU6tmJoLM9fV'
ACCESS_SECRET = 'N8xkvZAgwwhRFk5GjOkFVqEAIRVwlQMmhwFTw2Re1p3T5'

# Make the twitter object
twitter = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)

# Make the Klout object
k = Klout('rkyutwv2tna2tkffymmefkuj', secure=True)

personality_insights = PersonalityInsightsV3(
  version='2016-10-20',
  username='f5b5d68f-22f8-46b8-9323-834de272a20b',
  password='Y8lZLGEw8WUY')

def findAccounts(orgString, k):
	searchString = '@'+orgString
	accounts = twitter.search_users(q=searchString, count=20)
	
	# contains (screenname, score)
	accountInfo = []
	print orgString
	for i in range(0, len(accounts)):
		print(accounts[i]['screen_name'])
		if(accounts[i]['protected']==False):
			try:
				kloutId = k.identity.klout(tw=accounts[i]['id_str']).get('id')
				score = k.user.score(kloutId=kloutId).get('score')
				accountInfo.append([accounts[i]['screen_name'], score])
				print "User's klout score is: %s" % (score)	
			except:
				print 'forbidden error'
		else:
			print 'private twitter page'
	sortedAccounts = sorted(accountInfo, key=lambda x: x[1])
	sortedAccounts = sortedAccounts[-3:]
	queryString = u''
	for x in sortedAccounts:
		queryString += getTweets(x[0])
	return analyzeTweets(queryString)



def getTweets( userString):
	tweetstring = u''
	user_timeline = twitter.get_user_timeline(screen_name=userString, count=1)
	tweetId = user_timeline[0]['id']
	lis = [tweetId] ## this is the latest starting tweet id
	for i in range(0, 1): ## iterate through all tweets
	## tweet extract method with the last list item as the max_id
	    user_timeline = twitter.get_user_timeline(screen_name=userString,
	    count=10, include_rts=False, max_id=lis[-1])
	    ##ctime.sleep(300) ## 5 minute rest between api calls

	    for tweet in user_timeline:
	        #print tweet['text'] ## print the tweet
	        lis.append(tweet['id']) ## append tweet id's
	        tweetstring += tweet['text']+u'  '
  	return tweetstring
  	

def analyzeTweets(tweets):
	tweets = tweets.decode('utf-8', 'ignore')
	profile = personality_insights.profile(
		tweets, content_type='text/plain',
		raw_scores=True, consumption_preferences=True)
	print(profile['word_count'])
	return profile

if(len(sys.argv)>1):
	argument = sys.argv[1]+''
	accountsToExtract = findAccounts(argument, k)
