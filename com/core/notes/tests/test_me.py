

from django.conf import settings
from django.test import TestCase


class ModelsTestCase(TestCase):

    def test_me(self):
        print(settings.SECRET_TEST_EMAIL)
        print(settings.SECRET_TEST_PWD)