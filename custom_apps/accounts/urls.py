from django.contrib import admin
from django.conf.urls import url
from accounts import views

urlpatterns = [
    url(r'^forgot-password', views.forgot_password, name='forgot'),
    url(r'^signup', views.signup_user, name='signup'),
    url(r'^login', views.login_user, name='login'),
    url(r'^logout', views.logout_user, name='logout'),
    url(r'^profile', views.ProfileView.as_view(), name='profile'),
    url(r'^$', views.accounts_redirection, name='accounts_redirection'),
]