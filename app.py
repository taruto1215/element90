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
    TextMessage, TextSendMessage, ImageSendMessage, TemplateSendMessage,
    ButtonsTemplate, CarouselTemplate, CarouselColumn,
    PostbackTemplateAction
)
try:
    import MySQLdb
except:
    import pymysql
    pymysql.install_as_MySQLdb()
    import MySQLdb
import json
import os
import codecs
import sys
import schedule
import time

#=======module you made========
import element
#==============================

#Flask+++++++++++++++++++++++++
app = Flask(__name__)
#++++++++++++++++++++++++++++++

#環境変数取得=====================================================
YOUR_CHANNEL_ACCESS_TOKEN = os.getenv('LINE_CHANNEL_ACCESS_TOKEN')
YOUR_CHANNEL_SECRET =  os.getenv('LINE_CHANNEL_SECRET')
#=================================================================

#Read Access token and channel secret=============================
line_bot_api = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(YOUR_CHANNEL_SECRET)
#=================================================================

#This is test part
#If it shows 'Hello world' when you access 'https://element90bot.herokuapp.com/test', it work well++
@app.route('/test')
def test():
    return('Hello world')
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


#To notify LINE API of existing this application+++++++++++++++++
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
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#Responses when a message came=================
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):

    message = element.get_ele(event.message.text.rstrip())

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=message))

    if (event.message.text == '周期表') or (event.message.text == 'periodic table'):
        line_bot_api.reply_message(
            event.reply_token,
            ImageSendMessage(
                original_content_url='https://www.google.com/imgres?imgurl=https%3A%2F%2Fupload.wikimedia.org%2Fwikipedia%2Fcommons%2Fthumb%2F6%2F64%2FPeriodic_table_%252818-col%252C_enwiki%2529%252C_black_and_white.png%2F240px-Periodic_table_%252818-col%252C_enwiki%2529%252C_black_and_white.png&imgrefurl=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FHistory_of_the_periodic_table&docid=F0n4GzblXq2GGM&tbnid=sJxV9ryRNfVtDM%3A&vet=10ahUKEwiWu6Dy2YvhAhUJXbwKHaU-CoUQMwi4AShCMEI..i&w=240&h=150&bih=968&biw=1920&q=periodic%20table%20image&ved=0ahUKEwiWu6Dy2YvhAhUJXbwKHaU-CoUQMwi4AShCMEI&iact=mrc&uact=8',
                preview_image_url='https://www.google.com/imgres?imgurl=https%3A%2F%2Fupload.wikimedia.org%2Fwikipedia%2Fcommons%2Fthumb%2F6%2F64%2FPeriodic_table_%252818-col%252C_enwiki%2529%252C_black_and_white.png%2F240px-Periodic_table_%252818-col%252C_enwiki%2529%252C_black_and_white.png&imgrefurl=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FHistory_of_the_periodic_table&docid=F0n4GzblXq2GGM&tbnid=sJxV9ryRNfVtDM%3A&vet=10ahUKEwiWu6Dy2YvhAhUJXbwKHaU-CoUQMwi4AShCMEI..i&w=240&h=150&bih=968&biw=1920&q=periodic%20table%20image&ved=0ahUKEwiWu6Dy2YvhAhUJXbwKHaU-CoUQMwi4AShCMEI&iact=mrc&uact=8'))

#=============================================

#Execute this application here++++++++++++++++
if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
#+++++++++++++++++++++++++++++++++++++++++++++
