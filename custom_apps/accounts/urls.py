from django.contrib import admin
from django.conf.urls import url
from accounts import views

urlpatterns = [
    url(r'^change-password/$', views.change_password, name='change_password'),
    url(r'^forgot-password/$', views.forgot_password, name='forgot'),
    url(r'^profile/$', views.ProfileView.as_view(), name='profile'),
    url(r'^signup/$', views.signup_user, name='signup'),
    url(r'^logout/$', views.logout_user, name='logout'),
    url(r'^login/$', views.login_user, name='login'),
    # url(r'^profile/edit/', views.ProfileEditView.as_view(), name='profile_edit'),
    url(r'^$', views.accounts_redirection, name='accounts_redirection'),
]