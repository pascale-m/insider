from twython import Twython 
import time 

''' Go to https://apps.twitter.com/ to register your app to get your api keys '''
CONSUMER_KEY = 'GdVE1KUrR9A3Cj3OodaGARFaw'
CONSUMER_SECRET = 'XgLJvHMFP5EbnZxJDs9o92nTILyDgCwSK21e3zrfRNb4spO32t'
ACCESS_KEY = '740727093382643713-DtNLbAyqa2CGKhGcdGOsU6tmJoLM9fV'
ACCESS_SECRET = 'N8xkvZAgwwhRFk5GjOkFVqEAIRVwlQMmhwFTw2Re1p3T5'

twitter = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)

personality_insights = PersonalityInsightsV3(
  version='2016-10-20',
  username='f5b5d68f-22f8-46b8-9323-834de272a20b',
  password='Y8lZLGEw8WUY')



def getTweets( userString):
	user_timeline = twitter.get_user_timeline(screen_name=userString, count=1)
	tweetId = user_timeline[0]['id']
	lis = [tweetId] ## this is the latest starting tweet id
	for i in range(0, 1): ## iterate through all tweets
	## tweet extract method with the last list item as the max_id
	    user_timeline = twitter.get_user_timeline(screen_name=userString,
	    count=2, include_rts=False, max_id=lis[-1])
	    ##ctime.sleep(300) ## 5 minute rest between api calls

	    for tweet in user_timeline:
	        print tweet['text'] ## print the tweet
	        lis.append(tweet['id']) ## append tweet id's
	with open(join(dirname(__file__), './profile.json')) as profile_json:
  		profile = personality_insights.profile(
    		profile_json.read(), content_type='application/json',
    		raw_scores=True, consumption_preferences=True)

print(json.dumps(profile, indent=2))



getTweets('cellar4door');
