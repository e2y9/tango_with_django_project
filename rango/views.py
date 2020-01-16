from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage matches to {{ boldmessage }} in the template!
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render(request, 'rango/index.html', context=context_dict)

def test_page(request):
    new_context_dict = {'newboldmessage': 'Hey hey, ho ho, woah woah!'}
    return render(request, 'rango/test_page.html', context=new_context_dict)


    # old HttpResponse way of displaying page:
    # return HttpResponse("Rango says hey there partner! <a href='/rango/about'>About</a>")

def about(request):
    return render(request, 'rango/about.html', {})
