#!/usr/bin/env python
import configparser
import psycopg2
from runtext import *

config = configparser.ConfigParser()
config.read('config.ini')

HOST = config['sql']['HOST']
DB = config['sql']['DB']
PORT = config['sql']['PORT']
UN = config['sql']['UN']
PW = config['sql']['PW']

runner = RunText()
runner.run()

conn = psycopg2.connect(host=HOST,dbname=DB,port=PORT,user=UN,password=PW)
cur = conn.cursor()

cur.execute("SELECT * FROM tweets WHERE approved = true")
rows = cur.fetchall()

for tweet in rows:
	print(bytes.fromhex(tweet[0]).decode())


# close
cur.close()
conn.close()
