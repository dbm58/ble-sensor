#!/usr/bin/env python

import inspect
import json
import string
import sys

from Adafruit_IO import Client, RequestError, Feed, Data

import app_secrets

def _send(aio, feed_name, value):
    if value is None:
        return

    try:
        feed = aio.feeds(feed_name)
        print('feed exists')
        print(feed)
    except RequestError:
        #  The feed doesn't exist.  Create it!
        print('feed doesn\'t exist')
        new_feed = Feed(name=feed_name)
        feed = aio.create_feed(new_feed)
    aio.send_data(feed.key, value)


with open('weather.json') as f:
    x = json.load(f)
temp = x['current_condition'][0]['temp_F']
print(temp)

aio = Client(app_secrets.AIO_USER_NAME, app_secrets.AIO_KEY)
_send(aio, 'weather', temp);

