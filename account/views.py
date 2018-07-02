from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


def home(request):
    name = 'Aadway'
    args = {'name': name}
    return render(request, 'account/home.html', args)


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/account')
    else:
        form = UserCreationForm()
        args = {'form': form}
        return render(request, 'account/reg_form.html', args)
