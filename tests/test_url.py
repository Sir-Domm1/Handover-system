import pytest
from django.test import SimpleTestCase
from django.urls import resolve,reverse
from home.views import Home,Handover_list,Completed_handovers,Notice,Notice_Display,opinion,data
from Auth.views import Login,Logout, Signup
from django.core import mail
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes

class TestUrls(SimpleTestCase):
    def test_home_url_is_resolved(self):
        url=reverse('home-page')
        self.assertEqual(resolve(url).func,Home)

    def test_handover_url_is_resolved(self):
        url=reverse('handover-page')
        self.assertEqual(resolve(url).func,Handover_list)

    def test_completed_task_url_is_resolved(self):
        url=reverse('completed-handovers')
        self.assertEqual(resolve(url).func,Completed_handovers)

    def test_notice_url_is_resolved(self):
        url=reverse('notice-page')
        self.assertEqual(resolve(url).func,Notice)

    def test_notice_display_url_is_resolved(self):
        url=reverse('notice-display-page')
        self.assertEqual(resolve(url).func,Notice_Display)

    def test_comments_url_is_resolved(self):
        pk=1
        url=reverse('comment-page', kwargs={'pk':pk} )
        resolved_view=resolve(url).func
        self.assertEqual(resolved_view,opinion)

    def test_specifics_url_is_resolved(self):
        pk=1
        url=reverse('specifics-page',kwargs={'pk':pk})
        resolved=resolve(url).func
        self.assertEqual(resolved,data)

        #Testing urls for Auth app
    def test_login(self):
        url=reverse('Login')
        self.assertEqual(resolve(url).func,Login)

    def test_logout(self):
        url=reverse('Logout')
        self.assertEqual(resolve(url).func,Logout)

    def test_Signup(self):
        url=reverse('signup')
        self.assertEqual(resolve(url).func,Signup)

@pytest.mark.django_db
def test_PasswordResetView(client):
    user=User.objects.create_user('Josh','josh57@gmail.com','password123')
    response=client.post(reverse('reset_password'),{'email':'josh57@gmail.com'})
    assert response.status_code == 302
    assert len(mail.outbox) == 1
    assert mail.outbox[0].subject == 'Password reset on testserver'
    assert 'reset' in mail.outbox[0].body
    
@pytest.mark.django_db
def test_PasswordResetDoneView(client):
    user=User.objects.create_user('Josh','josh57@gmail.com','password123')
    response=client.post(reverse('reset_password'),{'email':'josh57@gmail.com'})
    assert response.status_code == 302
    assert mail.outbox[0].subject == 'Password reset on testserver'
    assert 'reset' in mail.outbox[0].body
    
@pytest.mark.django_db
def test_PasswordResetCompleteView(client):
    url=reverse('password_reset_complete')
    response=client.get(url)
    assert response.status_code==200
    assert 'reset_password_complete.html' in [t.name for t in response.templates]

@pytest.mark.django_db
def test_PasswordResetConfirmView(client):
    user=User.objects.create_user('Josh','josh57@gmail.com','password123')
    uidb64=urlsafe_base64_encode(force_bytes(user.pk))
    token=default_token_generator.make_token(user)

    url=reverse('password_reset_confirm',kwargs={'uidb64': uidb64, 'token': token})
    response=client.get(url)
    response.status_code==200
    #assert 'reset.html' in [t.name for t in response.templates]