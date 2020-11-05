import tweepy
import sched, time
from time import sleep
from urllib.parse import quote_plus

# Twitter Dev API
# Replace the words with your auth tokens from Twitter Development Dashboard here. There should be 4. You can ignore the bearer token for this code.
auth = tweepy.OAuthHandler('API KEY','API SECRET KEY')
auth.set_access_token('ACCESS TOKEN', 'ACCESS TOKEN SECRET')
api = tweepy.API(auth, wait_on_rate_limit=True)

def generate_query(keywords, modifiers):
    joined_terms = " OR ".join(keywords)
    mods = " ".join(modifiers)
    return quote_plus(f"({joined_terms}) {mods}")
#Put your key phrase or phrases here. You don't need to worry about url encoding - just put the words straight in. 
search_terms = ["please", "separate", "phrases", "like", "this"]
#Add modifiers here if you want. If you don't need it, remove it. It's pretty simple. "-phrase" will ignore all tweets with the phrases. "lang:xx" will only use tweets in that language (it uses ISO 639-1 international codes) and "-lang:xx" will exclude tweets written in that language. Replace xx with the language code. If you require other modifiers, you can find them on the Standard Operators page in Twitter for Developers.
modifiers = ["separate", "like", "before"]
search_query = generate_query(search_terms, modifiers)

def phrase_search(items):
    return list(tweepy.Cursor(api.search, q=search_query).items(items))

s = sched.scheduler(time.time, time.sleep)
to_retweet = phrase_search(20)
def retweet_task(scheduler, tweet_list):
    print(len(tweet_list))
    try:
        tweet = tweet_list[0]
    except IndexError:
        tweet_list = phrase_search(20)
        tweet = tweet_list[0]
        # The seconds interval is how regularly your bot will tweet. I recommend you keep this about 120, as twitter only allows a maximum of 1000 tweets a day, broken down into 30 minute intervals. That's 20.83 tweets per half hour = ~1 tweet every 2 minutes. You can change it, but at your own risk.
    seconds_interval = 200

    try:
        print(tweet_list[0]._json['text'])
        tweet.retweet()
    except tweepy.TweepError as error:
        print('\nError. Retweet not successful. Reason: ')
        print(error.reason)
        seconds_interval = 1
    except AttributeError:
        pass

    del tweet_list[0]
    print(len(tweet_list))
    
    scheduler.enter(seconds_interval, 1, retweet_task, argument=(scheduler, tweet_list))
    

s.enter(15, 1, retweet_task, argument=(s, to_retweet))
s.run()