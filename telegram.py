import os
import json
import requests

bot_token = os.environ['bot_token']
channel_id = os.environ['channel_id']
admin_id = ''
footer = os.environ['footer']


def msg_to_admin(args):
    text_caps = ''.join(args)
    requests.post(
        url='https://api.telegram.org/bot{0}/{1}'.format(
            bot_token, 'sendMessage'),
        data={'chat_id': admin_id, 'text': text_caps}
    )


def send_app(url, cat):
    message = "{link}\n\n{cat}\n\n{footer}".format(link=url, cat=cat, footer=footer)
    return requests.post(
        url='https://api.telegram.org/bot{0}/{1}'.format(
            bot_token, 'sendMessage'),
        data={'chat_id': channel_id, 'text': message}
    )
