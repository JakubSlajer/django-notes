from django.contrib.auth.models import User, Group
from rest_framework import serializers

from .models import Note, UserProfile


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'url', 'username', 'first_name', 'last_name', 'email', 'date_joined']


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserProfile
        user = UserSerializer
        fields = ['id', 'url', 'user', 'birthdate', 'favourite_animal']




class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'url', 'name']


class NoteSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Note
        fields = ['id', 'url', 'author', 'subject', 'content', 'contentType',
                  'createdT', 'editedT', 'status']
