# 247retweetbot
A bot that will retweet tweets containing a phrase (or multiple phrases) every ~2 minutes. Customizable. 

This bot is compatible with the Twitter API beta & 1.1 version.

You will need to have an activated Twitter for Developers account. Apply here with the account you want to convert into a bot. The bot will only post to the account you signed up for. Do not sign up with your personal account if you don't want it to be a bot. Make a new account and apply with that one.
 https://developer.twitter.com/en/apply-for-access

You will need to install tweepy before using. All you have to do is type "pip install tweepy" into your python terminal, and it will work.

Download the blank.py file  and open it in your chosen program. I used Microsoft Visual Studio Code, and I'm unfamiliar with other programs.

Make sure to fill in the Twitter Auth codes. There's four of them.

As explained in the comments in the code, Twitter has a tweet limit. 1000 tweets per day, including retweets. This rate limit is maintained every half hour, so your account can post 20.86 tweets a half hour. The timer is automatically set to retweet a tweet from the search query every 200 seconds, but you can make it higher or lower. Making it lower than ~120seconds will almost certainly make you hit the tweet limit, but the choice is there.

If you want to customise the search query, have a look here for options to implement.
https://developer.twitter.com/en/docs/twitter-api/v1/rules-and-filtering/overview/standard-operators

# Known errors/bugs

The bot cannot currently retweet things in reverse chronological order AKA the latest tweets. It tweets whatever is avaliable when it searches. Which can mean it sometimes retweets tweets made anywhere from 30 seconds ago all the way to 2009 (my bot personally has never gone to 2009, the oldest was 2017). I'm asking TwitterCommunity on advice for this.

The bot will sometimes retweet tweets from accounts with your keyphrase. If your bot retweets any tweet with the word "frog" in it, every now and again, it'll retweet a tweet made by @froguser123. I don't know why this happens, but I'm assuming it's an issue with twitter's search function. Not sure whether I can fix it or not, but again, I've asked TwitterCommunity. I'll update both of these bugs once I receive info on whether it's fixable or not. 
