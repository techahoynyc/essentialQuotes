# essentialQuotes

## Description
During difficult and uncertain times, messages of hope, strength, and encouragement can have a meaningful impact. EssentialQuotes is a project designed to capture outpouring of community support from tweets and simple messages. Received messages are displayed on a chain of 64x32 RGB matrixes.

You can read more about the project on Hackster.io.  

## Requirements
* hzeller's great [rpi-rgb-led-matrix repo](https://github.com/hzeller/rpi-rgb-led-matrix)
* Postgres back-end DATABASE_NAME

## Installation
This repository uses submodules so you'll need to clone with:
```
git clone --recursive https://github.com/techahoynyc/essentialQuotes
```
If you didn't use the `--recursive` argument you can pull down the [rpi-rgb-led-matrix repo](https://github.com/hzeller/rpi-rgb-led-matrix) with:
```
git submodule update --init --recursive
```

## Files
* **README.md**: This file.
* **getTweets.py**: 
* **showQuotes.py**:
* **showTestQuote.py**:
* **windowDisplay.py**:
