"""Defines URL patterns for users"""

from django.conf.urls import url
from django.contrib.auth import login
from django.contrib.auth import logout

from . import views

urlpatterns = [
    # Login page
    url(r'^login/$', login, {'template_name': 'users/login.html'},
        name='login'),
    # Logout page
    url(r'^logout/$', views.logout_view, name='logout'),
]