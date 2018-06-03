# from django.contrib.auth.hashers import check_password
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

from django.core.exceptions import ValidationError



class EmailAuthenticationBackend(ModelBackend):
    """
    This specifies to Django that it has
    to use the Email Authentication backend
    in order to work with users.

    The authenticate() an get_user() are then
    used in the views in order to authenticate
    and get users.

    AUTH_USER_MODEL = 'accounts.MyUser'
    AUTHENTICATION_BACKENDS = ('accounts.backends.EmailAuthenticationBackend',)
    """
    def authenticate(self, request, email=None, password=None):
        MyUser = get_user_model()
        
        try:
            # Check the email/password
            # and return a user
            user = MyUser.objects.get(email=email)

            if user.check_password(password):
                return user
        
        except MyUser.DoesNotExist:
            return None

    def get_user(self, user_id):
        MyUser = get_user_model()
        try:
            return MyUser.objects.get(pk=user_id)
            
        except MyUser.DoesNotExist:
            return None
