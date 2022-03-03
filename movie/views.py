from django.shortcuts import render
from django.shortcuts import HttpResponse

def home(request):
    #return render(request, 'home.html', {'name':'Greg Lim'})
    searchTerm = request.GET.get('searchMovie')
    return render(request, 'home.html', {'searchTerm':searchTerm})

def about(request):
    return HttpResponse('<h1>Welcome to About Page</h1>')
