import pytz
import datetime

from django.core.management import call_command
from django.test import TestCase
from django.contrib.auth.models import User

from core.notes.models import UserProfile, Note, ContentType, NoteStatus


class ModelsTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):

        # Load fixtures
        call_command('loaddata', 'testdata.yaml', verbosity=0)
        super().setUpTestData()


    def test_retrieve_users(self):
        self.assertEquals(len(list(User.objects.all())), 2)
        self.assertEquals(list(User.objects.all()), [User.objects.get(pk=1), User.objects.get(pk=2)])
        self.assertIn(User.objects.get(username="TestAdmin"), list(User.objects.all()))
        self.assertIn(User.objects.get(username="TestUser"), list(User.objects.all()))

    def test_retrieve_user_profiles(self):
        self.assertEquals(len(list(UserProfile.objects.all())), 2)
        self.assertEquals(list(UserProfile.objects.all()), [UserProfile.objects.get(pk=1), UserProfile.objects.get(pk=2)])
        self.assertIn(UserProfile.objects.get(user=1), list(UserProfile.objects.all()))
        self.assertIn(UserProfile.objects.get(user=2), list(UserProfile.objects.all()))

    def test_retrieve_notes(self):
        self.assertEquals(len(list(Note.objects.all())), 2)
        self.assertEquals(list(Note.objects.all()), [Note.objects.get(pk=1), Note.objects.get(pk=2)])
        self.assertIn(Note.objects.get(subject="whiskey diet"), list(Note.objects.all()))
        self.assertIn(Note.objects.get(subject="tortoise"), list(Note.objects.all()))

    def test_me(self):
        None

    def test_me_another(self):
        None

    def test_model(self):
        None

    def tearDown(self):
        super().tearDown()


