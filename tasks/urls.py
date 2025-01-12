from django.urls import path
from . import views

urlpatterns = [
    path('accounts/login/', views.login_user, name='login'),  
    path('', views.home, name='home'),
    path('', views.tasks, name='tasks'),
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('tasks/', views.tasks, name='tasks'),
    path('create/', views.create_task, name='create_task'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('task/<int:task_id>/update/', views.update_task_status, name='update_task_status'),
    path('task/<int:task_id>/delete/', views.delete_task, name='delete_task'),
    path('tasks/', views.task_list, name='tasks'),
    path('create-task/', views.create_task, name='create_task'),
    path('register/', views.register, name='register'),
     path('chatbot/chat/', views.chatbot, name='chatbot'),
]
