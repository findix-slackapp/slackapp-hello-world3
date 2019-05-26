# coding: utf-8

from slackbot.bot import Bot
import threading
import schedule
import time
from godd_morning import GoodMornig

def main():
    bot = Bot()
    bot.run()

def goodMorning():
    gm = GoodMornig()
    channels = gm.belongChannelList()
    gm.postMessage(channels)

if __name__ == "__main__":
    print('start slackbot')
    thread_1 = threading.Thread(target=main)
    thread_1.start()

    print('start good morning')
    schedule.every().monday.at("00:00").do(goodMorning)
    schedule.every().tuesday.at("00:00").do(goodMorning)
    schedule.every().wednesday.at("00:00").do(goodMorning)
    schedule.every().thursday.at("00:00").do(goodMorning)
    schedule.every().friday.at("00:00").do(goodMorning)

    while True:
        schedule.run_pending()
        time.sleep(1)

