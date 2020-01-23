from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category
from rango.models import Page

def index(request):

    # Query the database for a list of ALL categories currently stored.
    # Order the categories by the number of likes in descending order.
    # Retrieve the top 5 only -- or all if less than 5.
    # Place the list in our context_dict dictionary (with our boldmessage!)
    # that will be passed to the template engine.
    category_list = Category.objects.order_by('-likes')[:5]
    pages_list = Page.objects.order_by('-views')[:5]

    # NOTES for ^^^
    # Here, the expression Category.objects.order_by('-likes')[:5] queries the Category
    # model to retrieve the top five categories. You can see that it uses the order_by()
    # method to sort by the number of likes in descending order. The - in -likes denotes
    # that we would like them in descending order (if we removed the - then the results
    # would be returned in ascending order).

    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage matches to {{ boldmessage }} in the template!
    context_dict = {}
    context_dict['boldmessage'] = 'Crunchy, creamy, cookie, candy, cupcake!'
    context_dict['categories'] = category_list
    context_dict['pages'] = pages_list

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

def show_category(request, category_name_slug):
    context_dict = {}

    try:
        category = Category.objects.get(slug=category_name_slug)
        pages = Page.objects.filter(category=category)
        context_dict['pages'] = pages
        context_dict['category'] = category

    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['pages'] = None

    return render(request, 'rango/category.html', context=context_dict)
