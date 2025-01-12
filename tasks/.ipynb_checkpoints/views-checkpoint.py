from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import TaskForm
from .models import Task
from .forms import UserRegistrationForm
from django.http import Http404
from django.contrib import messages
from django.http import JsonResponse


def home(request):
    return render(request, 'tasks/home.html')

def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'tasks/register.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            next_url = request.GET.get('next', 'tasks')  
            return redirect(next_url)
    else:
        form = AuthenticationForm()
    return render(request, 'tasks/login.html', {'form': form})

def logout_user(request):
    logout(request)
    return redirect('login')

@login_required
def tasks(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'tasks/tasks.html', {'tasks': tasks})

@login_required
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            messages.success(request, 'Task created successfully!')
            return redirect('tasks')
    else:
        form = TaskForm()
    return render(request, 'tasks/create_task.html', {'form': form})

@login_required
def delete_task(request, task_id):
    try:
        task = Task.objects.get(id=task_id, user=request.user)
        task.delete()
        messages.success(request, 'Task deleted successfully!')
    except Task.DoesNotExist:
        raise Http404("Task not found.")
    return redirect('tasks')


from django.shortcuts import render, get_object_or_404, redirect
from .models import Task

def update_task_status(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == 'POST':
        
        task.completed = not task.completed
        task.save()

    return redirect('tasks')  

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('tasks')
    else:
        form = UserRegistrationForm()
    return render(request, 'tasks/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('tasks')
    else:
        form = AuthenticationForm()
    return render(request, 'tasks/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)  
    return render(request, 'tasks/task_list.html', {'tasks': tasks})


def chatbot(request):
    user_query = request.GET.get('query', '').strip().lower()

    if not user_query:
        return JsonResponse({'response': 'Please provide a message.'})

    # Add conversational logic
    if 'hello' in user_query or 'hi' in user_query:
        bot_response = 'Hello! How can I assist you today?'
    elif 'create task' in user_query or 'add task' in user_query:
        bot_response = 'To create a new task, go to the "Tasks" section and click on "Create Task".'
    elif 'delete task' in user_query:
        bot_response = 'To delete a task, locate the task in your list and click on the delete icon next to it.'
    elif 'help' in user_query:
        bot_response = ('I am here to assist you! You can ask me about creating tasks, '
                        'deleting tasks, registration, or any issues you face.')
    elif 'register' in user_query or 'sign up' in user_query:
        bot_response = 'To register, click on the "Register" button in the top-right corner of the page.'
    elif 'goodbye' in user_query or 'bye' in user_query:
        bot_response = 'Goodbye! Let me know if you need anything else.'
    else:
        bot_response = ("I'm sorry, I didn't understand that. Could you please rephrase or ask something specific?")

    return JsonResponse({'response': bot_response})
