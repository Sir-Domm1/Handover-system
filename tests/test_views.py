from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.test.client import Client
from django.contrib.auth import login, logout
#from home.models import Handover
#from home.forms import handoverForm

class TestViews(TestCase):
    def setUp(self):
        self.user=User.objects.create_user(username='Domnic',password='12345')
        self.client.login(username='Domnic',password='12345')
        self.client=Client()


    #def test_Home_view(self):  
        #response=self.client.get(reverse('home-page'))
        #self.assertEqual(response.status_code,200)
        #self.assertTemplateUsed(response,'index.html')
        #self.assertIsInstance(response.context['form'],handoverForm)
        #self.assertFalse(response.context['form'].is_bound) 
        #self.assertRedirects(response, reverse('handover-page'))

#Testing login, logout and sign up authentication views
    def test_loinWithValidCredential(self):
        response=self.client.post(reverse('Login'),{
            'username':'Domnic',
            'password':'12345',

        })
        self.assertEqual(response.status_code,302)
        self.assertEqual(response.url,reverse('home-page'))
        self.assertTrue(response.wsgi_request.user.is_authenticated)

    def test_loginWithInvalidCredential(self):
          response=self.client.post(reverse('Login'),{
            'username':'Jackso',
            'password':'angukanayo',

        })
          self.assertEqual(response.status_code,302)
          #self.assertEqual(response.url,reverse('Login'))
          self.assertFalse(response.wsgi_request.user.is_authenticated)
          messages = list(response.wsgi_request._messages)
          self.assertEqual(len(messages), 1)
          self.assertEqual(str(messages[0]), 'Invalid credentials')
        
    #Testing Logout

    def test_logout(self):
        success_login=self.client.login(username='Domnic',password='12345')
        self.assertTrue(success_login)
        response=self.client.get(reverse('Logout'))

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('Login'))
        self.assertFalse(response.wsgi_request.user.is_authenticated)
        messages = list(response.wsgi_request._messages)
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'Successfully Logged out')

 #Testing for signup
    def test_signup(self):
        client=Client()
        response=self.client.post(reverse('signup'),{
            'Username':'Jacob',
            'Email':'Jacob56@gmail.com',
            'Password':'12345',
            'Confirm_Password':'12345'
        })

        self.assertEqual(response.status_code,302)
        

        #confirm user was created
        user=User.objects.get(username='Jacob')
        self.assertEqual(user.email,'Jacob56@gmail.com')

#Confirm email is already used.
    def test_ConfirmEmail(self):
        user=User.objects.create(username='Joan',email='Joan78@gmail.com',password='7890')
        response=self.client.post(reverse('signup'),{
            'Username':'James',
            'Email':'Joan78@gmail.com',
            'Password':'12345',
            'Confirm_Password':'12345'

        })
        self.assertEqual(response.status_code,302)
        self.assertEqual(response.url,reverse('signup'))
#Checking Error Messages
        messages = list(response.wsgi_request._messages)
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'Email already used, try another one')