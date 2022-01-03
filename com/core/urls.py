from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import TemplateView
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import routers
from .notes.views import UserViewSet, GroupViewSet, UserProfileViewSet, SignupView, NoteViewSet


router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('groups', GroupViewSet)
router.register('profiles', UserProfileViewSet)
router.register('notes', NoteViewSet)


urlpatterns = [
    # admin site urls ('/admin/..')
    path('admin/', admin.site.urls),

    # home single view url
    path('', TemplateView.as_view(template_name='home.html'), name='home'),

    # signup view url
    path('signup/', SignupView.as_view(), name='signup'),

    # django auth urls ('/login, /logout, etc.)'
    path('', include('django.contrib.auth.urls')),

    # access token url
    path('auth/oauth/token/', obtain_auth_token, name='token'),

    # rest framework api urls
    path('rest/resource/', include(router.urls))
]
