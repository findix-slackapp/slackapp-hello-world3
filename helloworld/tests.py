from django.test import TestCase, RequestFactory
from helloworld.views import HomePageView
from unittest import mock
import slackbot.dispatcher

class HelloWorldTestCase(TestCase):

    def setUp(self):
        self.factory = RequestFactory()

    def test_home_page(self):
        request = self.factory.get('/')
        response = HomePageView.as_view()(request)
        self.assertEqual(response.get('content-type'), 'text/html; charset=utf-8')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Congratulations')

    def test_slackbot(self):
        my_mock = mock.Mock()
        excepted = 'Hello World!'

        with mock.patch('slackbot.dispatcher', my_mock):
            import plugins.hello
            message = slackbot.dispatcher.Message(None, None)
            plugins.hello.mention_func(message)

        my_mock.Message(None, None).reply.assert_called_with(excepted)