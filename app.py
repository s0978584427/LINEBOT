# -*- coding: utf-8 -*-
"""


Line Bot聊天機器人
第一章 Line Bot申請與串接
Line Bot機器人串接與測試
"""
#載入LineBot所需要的套件
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('N0U3uYnEfm68Tfumug3KIwIJ9vcwOf14fBAOkWg0UGyT5Nn/DoBoE2yVRYFjVVDT1vbzRWRUTPEYLDWSV2Sp7+epIgp6kTFXrzDM6RL3cMqEWlNBF7QcHFq5Tmx+IT1xavP9f6Bu9fZ8X/TL9Jbk8AdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('58937a8133e8717c4687fee1ac72e145')

line_bot_api.push_message('Ufdb063e5098d4c50c6a325f6d7d408d6', TextSendMessage(text='你可以開始了'))

# 監聽所有來自 /callback 的 Post Request
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

#訊息傳遞區塊
##### 基本上程式編輯都在這個function #####
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = TextSendMessage(text=event.message.text)
    line_bot_api.reply_message(event.reply_token,message)

#主程式
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)