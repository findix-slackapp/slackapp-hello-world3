# coding: utf-8

from slackbot.bot import respond_to     # @botname: で反応するデコーダ
from slackbot.bot import listen_to      # チャネル内発言で反応するデコーダ
from slackbot.bot import default_reply  # 該当する応答がない場合に反応するデコーダ
import re

# @respond_to('string')     bot宛のメッセージ
#                           stringは正規表現が可能 「r'string'」
# @listen_to('string')      チャンネル内のbot宛以外の投稿
#                           @botname: では反応しないことに注意
#                           他の人へのメンションでは反応する
#                           正規表現可能
# @default_reply()          DEFAULT_REPLY と同じ働き
#                           正規表現を指定すると、他のデコーダにヒットせず、
#                           正規表現にマッチするときに反応
#                           ・・・なのだが、正規表現を指定するとエラーになる？

# message.reply('string')   @発言者名: string でメッセージを送信
# message.send('string')    string を送信
# message.react('icon_emoji')  発言者のメッセージにリアクション(スタンプ)する
#                               文字列中に':'はいらない
@respond_to('.*')
def mention_func(message):
    m_hello = re.match(r"^\S*こんにちは|こんにちわ\S*$", message.body['text'])
    m_gm = re.match(r"^\S*おはよう\S*$", message.body['text'])
    if m_hello:
        message.reply('こんにちは! :hand:')
    elif m_gm:
        message.reply('おはようございます:smile:') # メンション
    else:
        message.reply('Hello World!') # メンション

@listen_to('Hello World!')
def listen_func(message):
    message.send('Hi') # ただの投稿
    message.reply('Are you？')   # メンション