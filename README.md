# fb-post-bulk-delete
A python script to delete facebook posts in bulk

## Configuration
1. Open **app.py**
2. Enter you date in Unix timestamps in **until** and **since**
3. Enter your access_token in **access_token**

**Note:** To get your access token visit [https://developers.facebook.com/tools/explorer](https://developers.facebook.com/tools/explorer)

## Installation
Remember, you must have **python3** and **pip3** installed.
```
$ git clone https://github.com/sandipbgt/fb-post-bulk-delete.git
$ cd fb-post-bulk-delete
$ virtualenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ python app.py
```

## How to run
From your terminal type `python3 app.py` or `python app.py` depending upon how you have installed python on your system