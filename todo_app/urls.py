from django.urls import path
from . import views
urlpatterns = [
    path('',views.base,name='base'),
    path('home/',views.home,name='home'),
    path('add-todo',views.add_todo,name='add_todo'),
    path('todo_lists',views.view_todo_details,name='todo_lists'),
    path('completed_task',views.completed_task,name='completed_task'),
    path('mark_completed/<int:pk>/',views.mark_completed,name='mark_completed'),
    path('delete/<int:pk>/',views.delete,name='delete'),
    path('pending_task',views.pending_task,name='pending_task'),
]