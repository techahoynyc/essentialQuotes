import configparser
import psycopg2
from twython import Twython

config = configparser.ConfigParser()
config.read('config.ini')

APP_KEY = config['twitter']['APP_KEY']
APP_SECRET = config['twitter']['APP_SECRET']
ACCESS_TOKEN = config['twitter']['ACCESS_TOKEN']
ACCESS_SECRET = config['twitter']['ACCESS_SECRET']
HOST = config['sql']['HOST']
DB = config['sql']['DB']
PORT = config['sql']['PORT']
UN = config['sql']['UN']
PW = config['sql']['PW']

conn = psycopg2.connect(host=HOST,dbname=DB,port=PORT,user=UN,password=PW)
cur = conn.cursor()

twitter = Twython(APP_KEY, APP_SECRET, ACCESS_TOKEN, ACCESS_SECRET)

timeline = twitter.get_mentions_timeline(screen_name='techahoynyc', include_rts=False, count=1)

for tweet in timeline:
	thex = tweet['text'].encode('ascii','ignore').hex()
	tuser = tweet['user']['name']
	tdate = tweet['created_at']
	#print('hex: ' + thex + 'user: ' + tuser + 'date: ' + tdate)
	cur.execute("INSERT INTO tweets (tweet_hex,screen_name,created_at) values(%s, %s,%s) ON CONFLICT DO NOTHING", (thex,tuser,tdate))
conn.commit()

# close
cur.close()
conn.close()
