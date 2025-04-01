from django.urls import path
from . import views

urlpatterns = [
    path("", views.task_list, name="task_list"),
    path("register/", views.register, name="register"),
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),
    path("add_task/", views.add_task, name="add_task"),
    path("edit_task/<int:task_id>/", views.edit_task, name="edit_task"),
    path("delete_task/<int:task_id>/", views.delete_task, name="delete_task"),
   
]
