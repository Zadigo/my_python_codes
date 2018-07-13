from django import forms

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth import get_user_model

from django.forms import EmailField
from django.forms import widgets
from django.forms import Widget

from django.utils.translation import gettext, gettext_lazy as _

from accounts.models import MyUserProfile




MyUser = get_user_model()

class UserCreationForm(forms.ModelForm):
    """
    A form for creating new users. Includes all
    the required fields, plus a repeated password
    """
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = MyUser
        fields = ('email',)

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")

        return password2

    def save(self, commit=True):
        # Save the provided password 
        # in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])

        if commit:
            user.save()

        return user

class UserChangeForm(forms.ModelForm):
    """
    A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = MyUser
        fields = ('email', 'password',)

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]

class UserLoginForm(AuthenticationForm):
    username=EmailField(
        label=_("Email"),
        widget=widgets.EmailInput(attrs={'placeholder': 'Email...'})
    )
    password = forms.CharField(
        label= _("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'placeholder': 'Password...'}),
    )

    def clean2(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        if email is None and password:
            raise forms.ValidationError("Passwords don't match")     

        return self.cleaned_data

class UserSignupForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ('nom', 'prenom', 'email', 'password',)

class UserForgotPasswordForm(forms.Form):
    email = EmailField(
        widget=widgets.EmailInput(attrs={'placeholder':'email'})
    )

class MyUserTeacherProfileForm(forms.ModelForm):
    class Meta:
        model   = MyUserProfile
        fields  = ['__all__']

class MyUserLearnerProfileForm(forms.ModelForm):
    class Meta:
        model   = MyUserProfile
        fields  = []