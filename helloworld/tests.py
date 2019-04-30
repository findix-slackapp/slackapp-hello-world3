from django.test import TestCase, RequestFactory
from helloworld.views import HomePageView
from unittest import mock
import slackbot.dispatcher
import plugins.hello

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

    def assert_called_massage_reply(self, body, excepted):
        message = slackbot.dispatcher.Message(None, body)
        message.reply = mock.MagicMock()
        plugins.hello.mention_func(message)

        message.reply.assert_called_with(excepted)

