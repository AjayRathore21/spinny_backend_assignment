from django.urls import path
from store.views import *
from rest_framework.authtoken import views

urlpatterns = [
    path("auth_token/", views.obtain_auth_token, name="auth-token"),
]
