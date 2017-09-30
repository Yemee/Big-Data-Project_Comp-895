# -*- coding: utf-8 -*-      #necessary header to format string to UTF-8 encodig


#libraries required
import time
import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener

# load your app keys
consumer_key = "----"
access_token = "----"
access_token_secret = "----"
consumer_secret = "----"

#listener: get bunch of tweets from streaming
class StdOutListener(StreamListener):
	#method to read tweets
    def on_data(self, data):
    	#create a json file to store tweets, you can change location, name it as you like
        with open('HillaryClinton.csv', 'a') as f:
            try:
            	#show current tweets streaming
                print data
                f.write(data)
                f.write ('\n')
                return True
                #when limit (read API) is reached, wait for 15 minutes in order to continue
            except (tweepy.error.RateLimitError):
                time.sleep(60 * 15)
                print data
                f.write(data)
                f.write ('\n')
                #handling error 
            except BaseException as e:
                print("Error on_data: %s" % str(e))
        return True

    def on_error(self, status_code):
    	#handling TW API errors
        if status_code == 420:
            # returning False in on_error disconnects the stream
            return False
            # returning non-False reconnects the stream, with backoff.

#main of script
if __name__ == '__main__':
	#load listener class
    l = StdOutListener()
    
    #OAuthHandler instance
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
	
	#filter (or search) hashtag, read API for more options
    stream.filter(track=['HillaryClinton'], async=True)