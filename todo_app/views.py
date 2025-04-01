from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Task


# User Registration
def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if password != confirm_password:
            return render(request, "register.html", {"error": "Passwords do not match!"})

        if User.objects.filter(username=username).exists():
            return render(request, "register.html", {"error": "Username already exists!"})

        if len(password) < 6:
            return render(request, "register.html", {"error": "Password must be at least 6 characters long!"})

        User.objects.create_user(username=username, password=password)
        messages.success(request, "Account created successfully! You can now log in.")
        return redirect("login")

    return render(request, "register.html")

# User Login
def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect("task_list")
        return render(request, "login.html", {"error": "Invalid credentials"})
    return render(request, "login.html")

# User Logout
def user_logout(request):
    logout(request)
    return redirect("login")

# Display Tasks
@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    all_completed = tasks.exists() and all(task.completed for task in tasks)
    return render(request, "task_list.html", {"tasks": tasks, "all_completed": all_completed})

# Add Task
@login_required
def add_task(request):
    if request.method == "POST":
        title = request.POST.get("title")
        Task.objects.create(user=request.user, title=title)
        return redirect("task_list")
    return render(request, "add_task.html")

# Edit Task
@login_required
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    if request.method == "POST":
        task.title = request.POST.get("title")
        task.completed = "completed" in request.POST
        task.save()
        return redirect("task_list")
    return render(request, "edit_task.html", {"task": task})

# Delete Task
# @login_required
# def delete_task(request, task_id):
#     task = Task.object.get(id=task_id)
#     task.completed = True
#     task.save()
#     return redirect("task_list")
@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.delete()
    return redirect("task_list")
