#!/usr/bin/python
import configparser
import psycopg2
from rgbmatrix import RGBMatrix, RGBMatrixOptions, graphics
from windowDisplay import *

config = configparser.ConfigParser()
config.read('config.ini')

HOST = config['sql']['HOST']
DB = config['sql']['DB']
PORT = config['sql']['PORT']
UN = config['sql']['UN']
PW = config['sql']['PW']

wd = windowDisplay()
wd.initiate()

conn = psycopg2.connect(host=HOST,dbname=DB,port=PORT,user=UN,password=PW)
cur = conn.cursor()

cur.execute("SELECT * FROM tweets WHERE approved = true")
rows = cur.fetchall()

for tweet in rows:
	msg = tweet[0]
	print(msg) #debug
	wd.set(msg)
	wd.show()

# close
cur.close()
conn.close()
