import unittest
import json

from django.test import RequestFactory
from django.conf import settings

from django_jsend import JsendView


class SuccessJsendView(JsendView):
	def handle_request(self, request):
		return "Success message"

class ErrorJsendView(JsendView):
	def handle_request(self, request):
		raise Exception("Exception handling request")

class FailJsendView(JsendView):
	def handle_request(self, request):
		self.status = self.FAIL
		return "Incorrect data"

class DjangoJsendTestCase(unittest.TestCase):
	
	def setUp(self):
		self.factory = RequestFactory()
	
	def test_success_200(self):
		request = self.factory.get('/some/path/')
		response = SuccessJsendView.as_view()(request)
		
		self.assertEqual(response.status_code, 200)

	def test_success_json(self):
		request = self.factory.get('/some/path/')
		content = json.loads(SuccessJsendView.as_view()(request).content.decode("utf-8"))
		
		self.assertEqual(content['status'], JsendView.SUCCESS)
		self.assertEqual(content['data'], "Success message")

	def test_error_200(self):
		request = self.factory.get('/some/path/')
		response = ErrorJsendView.as_view()(request)
		
		self.assertEqual(response.status_code, 200)

	def test_error_json(self):
		request = self.factory.get('/some/path/')
		content = json.loads(ErrorJsendView.as_view()(request).content.decode("utf-8"))
		
		self.assertEqual(content['status'], JsendView.ERROR)
		self.assertEqual(content['message'], "Exception handling request")

	def test_fail_200(self):
		request = self.factory.get('/some/path/')
		response = FailJsendView.as_view()(request)
		
		self.assertEqual(response.status_code, 200)

	def test_fail_json(self):
		request = self.factory.get('/some/path/')
		content = json.loads(FailJsendView.as_view()(request).content.decode("utf-8"))
		
		self.assertEqual(content['status'], JsendView.FAIL)
		self.assertEqual(content['data'], "Incorrect data")


if __name__ == "__main__":
	settings.configure()
	unittest.main()