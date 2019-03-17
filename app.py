#!/usr/bin/env python
# coding: utf-8

from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    FollowEvent, UnfollowEvent, MessageEvent, PostbackEvent,
    TextMessage, TextSendMessage, TemplateSendMessage,
    ButtonsTemplate, CarouselTemplate, CarouselColumn,
    PostbackTemplateAction
)
from argparse import ArgumentParser
try:
    import MySQLdb
except:
    import pymysql
    pymysql.install_as_MySQLdb()
    import MySQLdb
import json
import pymatgen
import os
import codecs
import sys
import schedule
import time

app = Flask(__name__)

#環境変数取得

YOUR_CHANNEL_ACCESS_TOKEN = "1qF1HaYWqHabWRf2D7+uKgkP9yjnVmYBZ1qbeVAq1v5JAZktMMurT0v6kEfotADM6fDKw/3oRPuqjXR/rH9+de4VJyvlISAnUi86Z3PZxLpC6kTs/6cgvSzMXrjsKJS8J/xCZauhuo/c9vKvgun8oAdB04t89/1O/w1cDnyilFU="
YOUR_CHANNEL_SECRET =  "14ae0e84fd9edfce8ceb736e9270b59f"

YOUR_CHANNEL_ACCESS_TOKEN = os.getenv['YOUR_CHANNEL_ACCESS_TOKEN']
YOUR_CHANNEL_SECRET =  os.getenv['YOUR_CHANNEL_SECRET']


#REMOTE_HOST = os.getenv('REMOTE_HOST')
#REMOTE_DB_NAME = os.getenv('REMOTE_DB_NAME')
ÃÂ#REMOTE_DB_USER = os.getenv('REMOTE_DB_USER')
#REMOTE_DB_PASS = os.getenv('REMOTE_DB_PASS')
#REMOTE_DB_TB = 'heroku_8c9218b20533f08'

line_bot_api = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(YOUR_CHANNEL_SECRET)

#Connect database============================
#conn = MySQLdb.connect(user=REMOTE_DB_USER, passwd=REMOTE_DB_PASS, host=REMOTE_HOST, db=REMOTE_DB_NAME,charset='utf8')
#c = conn.cursor()

#sql = "SELECT user_id FROM heroku_8c9218b20533f08"
#c.execute(sql)
#userid = c.fetchall()

#c.close()
#conn.close()
#============================================

@app.route('/')
def hello_world():
    return('Hello world')

#to notify LINE API of existing this application
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


#a response when a message came
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":

    argv = ""
    try:
        argv = sys.argv[1]
    except:
        argv = "F"

    if argv == "T":
        go_weather()

    #    app.run()
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
