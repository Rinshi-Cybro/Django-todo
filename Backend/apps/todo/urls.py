from django.urls import path
from ..todo import views


urlpatterns = [
    path("", views.Todo, name='todo'),
    path('todo-delete/<int:id>/', views.DeleteTodo, name='todo-delete'),
    path('update-todo/<int:id>/', views.UpdateTodo, name='update-todo'),
]