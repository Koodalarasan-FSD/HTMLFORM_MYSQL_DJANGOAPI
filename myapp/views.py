from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import viewsets
from .models import User
from .forms import UserForm
from .serializers import UserSerializer

# API Views
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Template Views
def index(request):
    users = User.objects.all()
    return render(request, 'myapp/index.html', {'users': users})

def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = UserForm()
    return render(request, 'myapp/add_user.html', {'form': form})

def update_user(request, id):
    user = get_object_or_404(User, id=id)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = UserForm(instance=user)
    return render(request, 'myapp/update_user.html', {'form': form})
