from django.db import models
from django.contrib.auth.models import User

class CreatorType (models.TextChoices):
    """"""
    User = 'user',
    Group = 'group'

class ContentType (models.TextChoices):
    """"""
    Message = 'message',
    Reminder = 'reminder',
    Action = 'action',

class NoteStatus (models.TextChoices):
    """"""
    Draft = 'draft',
    Published = 'published',
    Withdrawn = 'withdrawn',


class UserProfile (models.Model):
    """"""
    objects = models.Manager()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthdate = models.DateField(max_length=30, null=True, blank=True)
    favourite_animal = models.CharField(max_length=100)

    def __str__(self):
        return self.user.__str__()


class Note (models.Model):
    """"""
    objects = models.Manager()
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    subject = models.CharField(max_length=50, null=True, blank=True)
    content = models.CharField(max_length=120, null=True, blank=True)
    content_type = models.CharField(max_length=30, choices=ContentType.choices, null=True, blank=True)
    created = models.DateTimeField(max_length=30, null=True, blank=True)
    edited = models.DateTimeField(max_length=30, null=True, blank=True)
    status = models.CharField(max_length=30, choices=NoteStatus.choices, null=True, blank=True)

    def __str__(self):
        return self.subject
