from django.db import models
from django.db.models.signals import post_save

from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

from django.core.exceptions import ValidationError

from django.dispatch import receiver




class MyUserManager(BaseUserManager):
    """
    This is the main manager for creating users in
    the application project.

    To do so, create methods that will act
    depending accordingly to create specific
    types of users or users in general.
    """
    def create_user(self, email, nom=None, prenom=None, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            nom=nom,
            prenom=prenom,
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    # Another method to create a specific type of user
    # def create_user_entreprise(self, email, nom=None, prenom=None, password=None, entreprise=True):
    #     if not email:
    #         raise ValueError('Users must have an email address')

    #     user = self.model(
    #         email=self.normalize_email(email),
    #         nom=nom,
    #         prenom=prenom,
    #     )
        
    #     user.entreprise=entreprise
    #     user.set_password(password)
    #     user.save(using=self._db)

    #     return user

    def create_superuser(self, email, password, nom=None, prenom=None):
        """
        Creates and saves a superuser with the given
        name, surname, email and password
        """
        user = self.create_user(
            email,
            password=password,
            nom=nom,
            prenom=prenom,
        )
        user.admin = True
        user.staff = True
        user.save(using=self._db)
        
        return user


class MyUser(AbstractBaseUser):
    email       = models.EmailField(verbose_name='email address', max_length=255, unique=True,)
    nom         = models.CharField(max_length=100, null=True, blank=True)
    prenom      = models.CharField(max_length=100, null=True, blank=True)
    
    active           = models.BooleanField(default=True)
    admin            = models.BooleanField(default=False)
    staff            = models.BooleanField(default=False)
    
    objects = MyUserManager()

    USERNAME_FIELD      = 'email'
    REQUIRED_FIELDS     = []

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_admin(self):
        return self.staff

    @property
    def is_staff(self):
        return self.staff


class MyUserProfile(models.Model):
    myuser_id           = models.ForeignKey(MyUser, on_delete=models.CASCADE)

    addresse            = models.CharField(max_length=100, blank=True, null=True)
    code_postal         = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.code_postal

# This creates the user profile
# automatically when a new user
# is created
@receiver(post_save, sender=MyUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        MyUserProfile.objects.create(myuser_id=instance)

# @receiver(post_save, sender=MyUser)
# def save_user_profile(sender, instance, **kwargs):
#     # instance.myuser_id.save()
#     pass

