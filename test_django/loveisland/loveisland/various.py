from django.contrib.admin import forms
from django.forms import fields
from django.contrib.auth import authenticate, login
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from django.contrib.admin.sites import AdminSite

class CustomAuthenticationForm(forms.AuthenticationForm):
    email = fields.EmailField()
    password = fields.CharField(min_length=10)

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        if email is not None and password:
            user_cache = authenticate(self.request, username=email, password=password)
            # login(self.request, user_cache)

class CustomAdminAuthenticationForm(CustomAuthenticationForm):
    pass

class CustomAdminSite(AdminSite):
    login_form = CustomAdminAuthenticationForm

# admin.autodiscover()
# admin.site.login_form = CustomAdminAuthenticationForm