from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group, User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import FormView
from rest_framework import permissions, viewsets
from rest_framework.authtoken.models import Token

from .models import Note, UserProfile
from .patches.permissions import IsAdminOrObjectOwner
from .serializers import (GroupSerializer, NoteSerializer, ProfileSerializer,
                          UserSerializer)


class IndexView(generic.CreateView):
    form_class = FormView
    success_url = reverse_lazy('home')
    template_name = 'registration/home.html'

class SignupView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class CreateProfileView(generic.CreateView):
    form_class = FormView
    success_url = reverse_lazy('profile-edit')
    template_name = 'profile-edit.html'


class UserViewSet(viewsets.ModelViewSet):
    """ API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminOrObjectOwner]

class GroupViewSet(viewsets.ModelViewSet):
    """ API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAdminUser]


class UserProfileViewSet(viewsets.ModelViewSet):
    """ API endpoint that allows users to be viewed or edited.
    """
    queryset = UserProfile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAdminOrObjectOwner]


class NoteViewSet(viewsets.ModelViewSet):
    """ API endpoint that allows notes to be viewed or edited.
    """
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [IsAdminOrObjectOwner]


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
