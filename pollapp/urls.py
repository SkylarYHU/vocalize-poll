from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('polls/', views.polls_list, name='polls_list'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'), 
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('create/', views.create_poll, name='create_poll'),
    path('poll/<int:poll_id>/delete/', views.delete_poll, name='delete_poll'),
    path('<int:poll_id>/', views.polls_detail, name='polls_detail'),
    path('<int:poll_id>/results/', views.poll_results, name='poll_results'),  
    path('random_poll/', views.random_poll, name='random_poll'),
]