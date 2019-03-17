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
YOUR_CHANNEL_SECRET =  "14ae0e84fd9edfce8ceb736e9270b59f
"

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

Â    u1 = "てんき"
    u2 = "天気"
    u1 = u1.encode('utf-8')
    u2 = u2.encode('utf-8')

#    if 'weather' or 'Weather' in str(event.message).decode('utf-8'):

    try:
        event.message.text = sys.argv[1]
    except:
        pass

    if (event.message.text == 'weather') or (event.message.text == 'Weather') or (event.message.text == '天気') or (event.message.text == 'てんき'):
        message = getweather.getweather()
        all = ""
        for i in message:
            if '雨' in i :
                all += '\n今日は雨が降りそうです！' + i + '\n\n'
            if '曇り' in i:
                all += '\n雲がかかる一日になりそうです！' + i + '\n\n'
            if '晴れ' in i:
                all += '\n晴れます！！！！！' + i + '\n\n'
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=all))

    elif (event.message.text == ''):
        message = getweather.getweather()
        all = ""
        for i in message:
            all += i + '\n'
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=all))

    else:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=event.message.text * 10))

@handler.add(FollowEvent)
def on_follow(event):
    reply_token = event.reply_token
ÃÂ    user_id = event.source.user_id
    profiles = line_bot_api.get_profile(user_id=user_id)
    display_name = profiles.display_name
    picture_url = profiles.picture_url
    status_message = profiles.status_message

    # DBへの保存
    try:
        conn = MySQLdb.connect(user=REMOTE_DB_USER, passwd=REMOTE_DB_PASS, host=REMOTE_HOST, db=REMOTE_DB_NAME,charset='utf8')
        c = conn.cursor()
        sql = "SELECT `id` FROM`"+REMOTE_DB_TB+"` WHERE `user_id` = '"+user_id+"';"
        c.execute(sql)
        ret = c.fetchall()
        if len(ret) == 0:
            sql = "INSERT INTO `"+REMOTE_DB_TB+"` (`user_id`, `display_name`, `status_message`, `status`)\
              VALUES ('"+user_id+"', '"+str(display_name)+"', '"+str(status_message)+"', 1);"
        elif len(ret) == 1:
            sql = "UPDATE `"+REMOTE_DB_TB+"` SET `display_name` = '"+str(display_name)+"',\
            `status_message` = '"+str(status_message)+"', `status` = '1' WHERE `user_id` = '"+user_id+"';"
        c.execute(sql)
        conn.commit()
    finally:
        conn.close()
        c.close()

    # メッセージの送信
    line_bot_api.reply_message(
        reply_token=reply_token,
        messages=TextSendMessage(text='登録Arigato!です!!')
    )



def go_weather(user_id=None, content=None):

#    if user_id is None or content is None:
#        return False
    if user_id is None or content is None:
        message = getweather.getweather()
        all = ""
        u_id = 'U33c8eba36ddd6aad11d2e0a29413ddf6'
        for i in message:
            if '雨' in i :
Â                all += '\n今日は雨が降りそうです！' + i + '\n'
            if 'り' in i:
                all += '\n雲がかかる一日になりそうです！' + i + '\n'
            else:
                all += + i + '\n'
        for i in userid:
            for j in i:
                line_bot_api.push_message(
                    to=str(j),
                    messages=TextSendMessage(text=all))


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
