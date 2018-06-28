from django.shortcuts import render, HttpResponse


def home(request):
    name = 'Aadway'
    args = {'name': name}
    return render(request, 'account/home.html', args)

