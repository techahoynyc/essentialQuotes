# essentialQuotes

## Description
During difficult and uncertain times, messages of hope, strength, and encouragement can have a meaningful impact. EssentialQuotes is a project designed to capture outpouring of community support from tweets and simple messages. Received messages are displayed on a chain of 64x32 RGB matrixes.

You can read more about the project on Hackster.io.  

## Requirements
* hzeller's great [rpi-rgb-led-matrix repo](https://github.com/hzeller/rpi-rgb-led-matrix)
* Postgres back-end DATABASE_NAME
* Twitter App

## Installation
1. This repository uses submodules so you'll need to clone with:
```
git clone --recursive https://github.com/techahoynyc/essentialQuotes
```
If you didn't use the `--recursive` argument you can pull down the [rpi-rgb-led-matrix repo](https://github.com/hzeller/rpi-rgb-led-matrix) with:
```
git submodule update --init --recursive
```
1. Create the `config.ini` file with the following format:
```
[twitter]
TW_NAME = <your twitter screen name>
TW_HASH = <your designed hash tag including # symbol>
APP_KEY = <your twitter app API Key>
APP_SECRET = <your twitter app API Secret>
ACCESS_TOKEN = <your twitter app Access Token>
ACCESS_SECRET = <your twitter app Access Secret>
[sql]
HOST = <your PSQL DB hostname>
DB = <your PSQL DB name>
PORT = 5432 <or your custom PSQL DB port>
UN = <your PSQL DB username>
PW = <your PSQL DB user's password>
[general]
DEFAULT_MSG = <your default message or instructions>
```  
1.


## Files
* **README.md**: This file
* **getTweets.py**: Checks your mentions timeline for tweets with the correct hashtag
* **showQuotes.py**: Grabs the recorded tweets and displays them
* **showTestQuote.py**: Shows a test quote
* **windowDisplay.py**: The class file for the matrix display
