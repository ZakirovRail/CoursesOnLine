from unittest import TestCase
from app import app


class BaseTest(TestCase):
    def setUp(self):
        app.testing = True  # we telling to the Flask that we are in the Testing mode
        self.app = app.test_client
