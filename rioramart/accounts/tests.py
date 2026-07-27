from django.test import TestCase

# Create your tests here.

#Test: successful registration
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

class RegisterTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_register_user(self):
        response = self.client.post(
            reverse('register'),
            {
                'username': 'testuser',
                'password1': 'StrongPassword123',
                'password2': 'StrongPassword123'
            }
        )

        # перевірка редіректу
        self.assertEqual(response.status_code, 302)

        # користувач створений
        self.assertEqual(User.objects.count(), 1)

        user = User.objects.first()
        self.assertEqual(user.username, 'testuser')
        
        
#Test: passwords do not match
def test_register_password_mismatch(self):
    response = self.client.post(
        reverse('register'),
        {
            'username': 'testuser',
            'password1': '123456',
            'password2': '654321'
        }
    )

    # користувач НЕ створений
    self.assertEqual(User.objects.count(), 0)

    # сторінка повертається з помилкою (не редірект)
    self.assertEqual(response.status_code, 200)
    
 
#Test: duplicate username    
def test_register_duplicate_user(self):
    User.objects.create_user(username='testuser', password='123456')

    response = self.client.post(
        reverse('register'),
        {
            'username': 'testuser',
            'password1': '12345678',
            'password2': '12345678'
        }
    )

    self.assertEqual(User.objects.count(), 1)