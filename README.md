* This program connects to twitter's REST API 
* Track tweets as a Regexp with the words inside a list
  * a space between the words mean a AND logic;
  * commas mean OR logic.

import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
import time
import json

class Listener(tweepy.StreamListener):

    def on_data(self, data):
        try:
            json_data = json.loads(data)
            created_at = json_data['created_at']
            text = json_data['text']
            lang = json_data['user']['lang']
            user_id = str(json_data['user']['id'])

            info_from_tweet = 'USER_ID:' + user_id + ' CREATED_AT:' + created_at + ' TEXT:' + text + \
                              ' LANG:' + lang
            save_file = open('tweetDB_using_lot_of_track_names.csv', 'a')
            save_file.write(str(info_from_tweet))
            save_file.write('\n')
            save_file.close()
            return True
        except BaseException, e:
            print('Failed', str(e))
            # print (str(e)
            time.sleep(5)
        
    def on_error(self, status_code):
        if status_code == 420:
            # retornar Falso ira desconectar o stream de dados
            return False

auth = OAuthHandler(consumer_key=consumer_key, consumer_secret=consumer_secret)
auth.set_access_token(access_token, access_token_secret)
twitterStream = Stream(auth, Listener())
twitterStream.filter(track=["depression", "depressive", "depressive life", "depressive mood", "depressive depression"],
                     async=True)
