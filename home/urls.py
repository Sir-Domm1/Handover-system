from django.urls import path
from. import views

urlpatterns = [
    path('home/', views.Home, name='home-page'),
    path('handover/', views.Handover_list, name='handover-page'),
    path('Completed Tasks/', views.Completed_handovers, name='completed-handovers'),
    path('Notice/', views.Notice, name='notice-page'),
    path('Notice-display/', views.Notice_Display, name='notice-display-page'),
    path('comments/<int:pk>/', views.opinion, name='comment-page'),
    #path('handover details/<int:pk>/', views.details, name='handover-details-page'),
    path('specifics/<int:pk>/',views.data,name='specifics-page'), 
   
]
