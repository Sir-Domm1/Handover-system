from django.urls import path
from.import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', views.Login, name='Login'),
    path('logout/', views.Logout, name='Logout'),
    path('signup/', views.Signup, name='signup'),
    path('reset_password/',auth_views.PasswordResetView.as_view(template_name='reset_password.html'),name='reset_password'),

    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name='reset_password_sent.html'),name='password_reset_done'),

    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='reset.html'),name='password_reset_confirm'),

    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name='reset_password_complete.html'),name='password_reset_complete'),
   
   
]