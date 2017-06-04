from django.http import HttpResponse
from django.shortcuts import render

def index(request):

    # Construct a citionary to pass to the template engine as it's contect.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    context_dict = {'boldmessage': "Crunch, creamy, cookie, candy, cupcake!"}
    return render (request, 'rango/index.html', context=context_dict)

def about(request):
    return HttpResponse("Rango says here is the about page. <a href='/rango'> Back to index</a>")
