import tweepy
import time

print('entrei')
consumer_key = 'PmwzArtWhHWGEMWlmC6eOoaGV'
consumer_secret = '4o3cLDGGXYaxOhhFv8uKKd1roAr6UatmWOYfzjLqmW02g6hWCM'
access_token = 	'986059156036706306-VnRTpYkm0qvgbdUD1urxleZjzUYZtur'
access_token_secret = '	kWyh6GBfGzOBBW2tRDNtnK7M4ussrsVYtoBpmpSNcC92A'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
twit_name_array=[]

for twit_name in twit_name_array:
 print('entrei')   
 api = tweepy.API(auth)
 t0= time.clock()

 data = api.rate_limit_status()
 user_followers_remaining = data['resources']['followers']['/followers/ids']['remaining']
 print(user_followers_remaining)
 id_i = twit_name[1]

 countpage = 0
 countx = 0

def limit_handled(cursor):
    while True:
        try:
            print('entrei')
            yield cursor.next()
        except BaseException as e:
            print('failed_on_CURSOR_NEXT', str(e))
            time.sleep(5)
            global api
            api = tweepy.API(auth)
            yield cursor.next()

