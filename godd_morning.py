import slack
import slackbot_settings

class GoodMornig:

    def __init__(self):
        self.client = slack.WebClient(token=slackbot_settings.API_TOKEN)

    def postMessage(self, channels):
        for channel in channels:
            self.client.chat_postMessage(channel=channel, text="おはようございます")

    def belongChannelList(self):
        channel_ids = []
        channels = self.client.api_call("channels.list")
        for channel in channels['channels']:
            if channel['members'].count("UCCDP5AH4") > 0:
                channel_ids.append(channel['id'])
        return channel_ids

if __name__ == "__main__":
    gm = GoodMornig()
    channels = gm.belongChannelList()
    gm.postMessage(channels)

