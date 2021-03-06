from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('day_mood/', views.day_mood),
    path('test_data/', views.test_data),
    path('activities/', views.activities),
    path('summary/', views.summary),
    

    path('index/', views.index, name='index'),

    # auth
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]