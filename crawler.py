# -*- coding: utf-8 -*-
import requests
from bs4 import *
import db
import time


pages = {'کتاب_ها_و_مطبوعات': 'https://cafebazaar.ir/lists/books-reference-new-apps',
         'آموزشی': 'https://cafebazaar.ir/lists/education-new-apps',
         'سرگرمی': 'https://cafebazaar.ir/lists/entertainment-new-apps',
         'مالی': 'https://cafebazaar.ir/lists/finance-new-apps',
         'آشپزی': 'https://cafebazaar.ir/lists/food-drink-new-apps',
         'سلامتی': 'https://cafebazaar.ir/lists/health-fitness-new-apps',
         'کودک': 'https://cafebazaar.ir/lists/kids-apps-new-apps',
         'سبک_زندگی': 'https://cafebazaar.ir/lists/lifestyle-new-apps',
         'نقشه_و_مسیریابی': 'https://cafebazaar.ir/lists/maps-navigation-new-apps',
         'پزشکی': 'https://cafebazaar.ir/lists/medical-new-apps',
         'صوت_و_تصویر': 'https://cafebazaar.ir/lists/music-audio-new-apps',
         'شخصی_سازی': 'https://cafebazaar.ir/lists/personalization-new-apps',
         'عکاسی': 'https://cafebazaar.ir/lists/photography-new-apps',
         'مذهبی': 'https://cafebazaar.ir/lists/religious-new-apps',
         'خرید': 'https://cafebazaar.ir/lists/shopping-new-apps',
         'اجتماعی': 'https://cafebazaar.ir/lists/social-new-apps',
         'ورزشی': 'https://cafebazaar.ir/lists/sports-new-apps',
         'ابزار': 'https://cafebazaar.ir/lists/tools-new-apps',
         'سفر': 'https://cafebazaar.ir/lists/travel-local-new-apps',
         'آب_و_هوا': 'https://cafebazaar.ir/lists/weather-new-apps'}


def parse(cat, url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0'
    }
    main_page = requests.get(url, headers=headers)
    parsed = BeautifulSoup(main_page.content, 'html.parser')
    list_container = parsed.find_all('div', class_='list-container__items')
    links = list_container[0].find_all('a')
    for link in links:
        app_url = 'https://cafebazaar.ir' + link['href']
        if not is_app_in_db(app_url):
            add_app_to_db(cat, app_url)


def add_app_to_db(cat, link, is_pub=False):
    app = {'cat': cat, 'link': link, 'is_pub': is_pub}
    x = db.apps.insert_one(app)
    print(x.inserted_id)


def is_app_in_db(url):
    query = {'link': url}
    if db.apps.count_documents(query) == 0:
        return False
    else:
        return True


for cat, url in pages.items():
    print(url)
    parse(cat, url)
    time.sleep(10)
