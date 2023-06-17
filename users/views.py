
from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from .forms import UserForm
from .models import User

def user_list(request):
    users = User.objects.all()
    return render(request, 'users/user_list.html', {'users': users})

def user_create(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserForm()
    return render(request, 'users/user_form.html', {'form': form})

def user_update(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return redirect('user_list')  

    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserForm(instance=user)

    return render(request, 'users/user_form.html', {'form': form})

def user_delete(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return redirect('user_list')   

    if request.method == 'POST':
        user.delete()
        return redirect('user_list')

    return render(request, 'users/user_confirm_delete.html', {'user': user})

 
