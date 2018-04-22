from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time


consumer_key = 'PmwzArtWhHWGEMWlmC6eOoaGV'
consumer_secret = '4o3cLDGGXYaxOhhFv8uKKd1roAr6UatmWOYfzjLqmW02g6hWCM'
access_token = 	'986059156036706306-VnRTpYkm0qvgbdUD1urxleZjzUYZtur'
access_token_secret = '	kWyh6GBfGzOBBW2tRDNtnK7M4ussrsVYtoBpmpSNcC92A'

class listener(StreamListener):

    def on_data(self, data):
        try:
            print(data)
            saveFile = open('tweetDB.csv', 'a')
            saveFile.write(data)
            saveFile.write('\n')
            saveFile.close()
            return True
        except BaseException, e:
            print 'failed ondata, ', str(e)
            time.sleep(5)
        
    def on_error(self, status):
        print(status)


auth = OAuthHandler(consumer_key, consumer_key)
auth.set_access_token(access_token, access_token)
twitterStream = Stream(auth, listener())
twitterStream.filter(track=["depression"])