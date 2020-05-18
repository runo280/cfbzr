# -*- coding: utf-8 -*-

import db
import telegram
import time

if __name__ == '__main__':

    unpublished_query = {'is_pub': False}
    set_published_query = {'$set': {'is_pub': True}}
    for x in db.apps.find(unpublished_query):
        url = x['link']
        cat = '#' + x['cat']
        telegram.send_app(url, cat)
        time.sleep(2)
        db.apps.update_one({'link': url}, set_published_query)
