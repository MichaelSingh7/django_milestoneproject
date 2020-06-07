from django.apps import apps
from django.test import TestCase
from .apps import MpConfig


class TestMpConfig(TestCase):
    def test_app(self):
        self.assertEqual("mp", MpConfig.name)
        self.assertEqual("mp", apps.get_app_config("mp").name)
