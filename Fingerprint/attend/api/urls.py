"""Fingerprint URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token
from .views import AttendancePostView, SmsUpdate, AttendancePostCreate, PostsView, PostsCreate, RegisterCreate, RegisterView , SuggestionCreate, SuggestionView, EventCreate, EventView, CreateUserView, UserLoginAPIView, RealAtendanceCreate, RealSignOutCreate, UploadNotesView

urlpatterns = [
    url(r'^$', AttendancePostCreate.as_view(), name='homesjuitcreate'),
    url(r'^(?P<pk>\d+)/$', AttendancePostView.as_view(), name='homesjuit'),
    url(r'^Posts/$', PostsCreate.as_view(), name='postcreate'),
    url(r'^Posts/(?P<pk>\d+)/$', PostsView.as_view(), name='postsjuit'),
    url(r'^api/auth/token-auth/', obtain_jwt_token),
    url(r'^Register/$', RegisterCreate.as_view(), name='Registercreate'),
    url(r'^Register/(?P<pk>\d+)/$', RegisterView.as_view(), name='Registersjuit'),
    url(r'^login/$', UserLoginAPIView.as_view(), name='login'),
    url(r'^Suggestion/$', SuggestionCreate.as_view(), name='Suggestioncreate'),
    url(r'^Suggestion/(?P<pk>\d+)/$', SuggestionView.as_view(), name='Suggestionsjuit'),
    url(r'^Event/$', EventCreate.as_view(), name='Eventcreate'),
    url(r'^UserCreate/$', CreateUserView.as_view(), name='Usercreate'),
    url(r'^Upload/$', UploadNotesView.as_view(), name='upload'),
    url(r'^Event/(?P<pk>\d+)/$', EventView.as_view(), name='Eventjuit'),
    url(r'^Real/$', RealAtendanceCreate.as_view(), name='Real'),
    url(r'^Sms/$', SmsUpdate.as_view(), name='Update'),
    url(r'^Sms/(?P<pk>\d+)/$', SmsUpdate.as_view(), name='Updated'),
    url(r'^Out/$', RealSignOutCreate.as_view(), name='SignOut'),
]
