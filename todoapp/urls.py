from django.urls import path
from . import views

app_name = 'todoapp'  # This sets the namespace

urlpatterns = [
    path('', views.todo_list, name='todo_list'),
    path('create_todo/', views.create_todo, name='create_todo'),
    path('delete_todo/<int:todo_id>/', views.delete_todo, name='delete_todo'),
    path('update_todo/<int:todo_id>/', views.update_todo, name='update_todo'),
]
