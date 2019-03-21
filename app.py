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
    PostbackTemplateAction, ImageMessage
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

    def imagesendmessage():
        image_message = ImageSendMessage(
            original_content_url='http://res.cloudinary.com/demo/image/upload/w_250,h_250,c_fill,f_auto/seagull.jpg',
            preview_image_url='http://res.cloudinary.com/demo/image/upload/w_250,h_250,c_fill,f_auto/seagull.jpg'
        )
        return (image_message)

    if (event.message.text == '周期表') or (event.message.text == 'periodic table'):
        image_message = imagesendmessage()
        line_bot_api.reply_message(
            event.reply_token,
            image_message = ImageSendMessage(
                original_content_url='http://res.cloudinary.com/demo/image/upload/w_250,h_250,c_fill,f_auto/seagull.jpg',
                preview_image_url='http://res.cloudinary.com/demo/image/upload/w_250,h_250,c_fill,f_auto/seagull.jpg'
            )
        )

#preview_image_url='https://upload.wikimedia.org/wikipedia/commons/thumb/d/d8/Electron_shell_001_Hydrogen_%28diatomic_nonmetal%29_-_no_label.svg/200px-Electron_shell_001_Hydrogen_%28diatomic_nonmetal%29_-_no_label.svg.png'
#=============================================

#Execute this application here++++++++++++++++
if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
#+++++++++++++++++++++++++++++++++++++++++++++
