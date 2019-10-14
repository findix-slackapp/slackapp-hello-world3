from django.test import TestCase, RequestFactory
from helloworld.views import HomePageView
from unittest import mock
import slackbot.dispatcher
import plugins.hello
import plugins.thanks
from godd_morning import GoodMornig
import slack
import slackbot_settings

class HelloWorldTestCase(TestCase):

    def setUp(self):
        self.factory = RequestFactory()

    def test_home_page(self):
        request = self.factory.get('/')
        response = HomePageView.as_view()(request)
        self.assertEqual(response.get('content-type'), 'text/html; charset=utf-8')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Congratulations')

    def test_mention_func_hello_world(self):
        body = {'text': 'hi'}
        excepted = 'Hello World!'
        self.assert_called_massage_reply(body, excepted)

    def test_mention_func_greeting(self):
        body = {'text': 'おはよう'}
        excepted = 'おはようございます:smile:'
        self.assert_called_massage_reply(body, excepted)

    def test_mention_func_thanks(self):
        body = {'text': 'ありがとう'}
        excepted = 'どういたしまして:smile:'
        self.assert_called_massage_reply(body, excepted)

    def assert_called_massage_reply(self, body, excepted):
        message = slackbot.dispatcher.Message(None, body)
        message.reply = mock.MagicMock()
        plugins.hello.mention_func(message)
        plugins.thanks.mention_func(message)

        message.reply.assert_called_with(excepted)

    # def test_good_morning_postMessage(self):
    #     gm = GoodMornig()
    #     client = gm.client
    #     client.chat_postMessage = mock.MagicMock()
    #     channels = gm.belongChannelList()
    #     gm.postMessage(channels)

    #     client.chat_postMessage.assert_called_with(channel="CHXS0FH5M",text="おはようございます",as_user=True)

    def test_post_return_no_user(self):
        data = {}
        request = self.factory.post('/', data)
        response = HomePageView.as_view()(request)
        self.assertEqual(response.get('content-type'), 'text/plain')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'no user')

    def test_post_return_unauthorized_user(self):
        data = {"user_id": "123"}
        request = self.factory.post('/', data)
        response = HomePageView.as_view()(request)
        self.assertEqual(response.get('content-type'), 'text/plain')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'unauthorized user')

    def test_post_return_no_parameter(self):
        data = {"user_id": "UB9AVTDT3"}
        request = self.factory.post('/', data)
        response = HomePageView.as_view()(request)
        self.assertEqual(response.get('content-type'), 'text/plain')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'no parameter')

    def test_post_return_invalid_parameter(self):
        data = {"user_id": "UB9AVTDT3", "text": "prj-slackapp-test"}
        request = self.factory.post('/', data)
        response = HomePageView.as_view()(request)
        self.assertEqual(response.get('content-type'), 'text/plain')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'invalid parameter')

    def test_post_return_no_message(self):
        data = {"user_id": "UB9AVTDT3", "text": "prj-slackapp-test,"}
        request = self.factory.post('/', data)
        response = HomePageView.as_view()(request)
        self.assertEqual(response.get('content-type'), 'text/plain')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'no message')

    def test_post_return_invalid_channel(self):
        data = {"user_id": "UB9AVTDT3", "text": "abc,test"}
        request = self.factory.post('/', data)
        response = HomePageView.as_view()(request)
        self.assertEqual(response.get('content-type'), 'text/plain')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'invalid channel')

    def test_post_call_chat_postMessage(self):
        client = slack.WebClient(token=slackbot_settings.API_TOKEN)
        slack.WebClient = mock.MagicMock(return_value=client)
        client.chat_postMessage = mock.MagicMock()

        data = {"user_id": "UB9AVTDT3", "text": "prj-slackapp-test,test"}
        request = self.factory.post('/', data)
        response = HomePageView.as_view()(request)
        self.assertEqual(response.get('content-type'), 'text/plain')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'test')
        client.chat_postMessage.assert_called_with(channel="CHXS0FH5M",text="test",as_user=True)
