from django.contrib.auth import get_user_model 
from django.test import TestCase


class CustomUserTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='alfredito', 
            email='myown@email.com', 
            password='elsecreto'
        )
        self.assertEqual(user.username, 'alfredito') 
        self.assertEqual(user.email, 'myown@email.com') 
        self.assertTrue(user.is_active) 
        self.assertFalse(user.is_staff) 
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self): 
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username='superalfredito', 
            email='another@email.com', 
            password='elsecreto'
        )
        self.assertEqual(admin_user.username, 'superalfredito') 
        self.assertEqual(admin_user.email, 'another@email.com') 
        self.assertTrue(admin_user.is_active) 
        self.assertTrue(admin_user.is_staff) 
        self.assertTrue(admin_user.is_superuser)