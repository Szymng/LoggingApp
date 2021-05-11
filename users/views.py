from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('basesites:index'))

def register(request):
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data = request.POST)

        if form.is_valid():
            new_user = form.save()
            authenticated_user = authenticate(username = new_user, password = request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('basesites:index'))

    context = {'form': form}
    return render(request, 'users/register.html', context)