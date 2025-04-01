
from django.contrib import admin
from django.urls import path, include

admin.site.site_header="To-Do List Admin"
admin.site.site_title="Admin"
admin.site.index_title="Welcome To-Do List Admin"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("todo_app.urls")),
]
