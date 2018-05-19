from django.test import TestCase

from accounts.models import MyUser

class UserTestCase(TestCase):
    def can_create_user_entreprise(self):
        user = MyUser.objects.create_user_entreprise('this@test.io', nom='Test', prenom='test')
        self.assertIsNone(user, 'None')
