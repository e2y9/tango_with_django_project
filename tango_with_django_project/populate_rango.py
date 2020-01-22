import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                        'tango_with_django_project.settings')

import django
django.setup()

from rango.models import Category, Page

def populate():
    # First, we will create lists of dictionaries containing the pages
    # we want to add into each category.
    # Then we will create a dictionary of dictionaries for our categories.
    # This might seem a little bit confusing, but it allows us to iterate
    # through each data structure, and add the data to our models.

    python_pages = [
        {'title': 'Official Python Tutorial',
        'url':'http://docs.python.org/3/tutorial/'},
        {'title':'How to Think like a Computer Scientist',
        'url':'http://www.greenteapress.com/thinkpython/'},
        {'title':'Learn Python in 10 Minutes',
        'url':'http://www.korokithakis.net/tutorials/python/'} ]

    django_pages =[
        {'title': 'Official Django Tutorial',
        'url':'https://docs.djangoproject.com/en/2.1/intro/tutorial01/'},
        {'title':'Django Rocks',
        'url':'http://www.djangorocks.com/'},
        {'title':'How to Tango with Django',
        'url':'http://www.tangowithdjango.com/'} ]

    other_pages = [
        {'title':'Bottle',
        'url':'http://bottlepy.org/docs/dev/'},
        {'title':'Flask',
        'url':'http://flask.pocoo.org'} ]

    cats = {'Python': {'pages': python_pages, 'views': 0, 'likes': 0},
            'Django': {'pages': django_pages, 'views': 0, 'likes': 0},
            'Other Frameworks': {'pages': other_pages, 'views': 0, 'likes': 0} }

# If you want to add more categories or pages,
# add them to the dictionaries above.
# The code below goes through the cats dictionary, then adds each category,
# and then adds all the associated pages for that category.
    for cat, cat_data in cats.items():
        c = add_cat(cat, cat_data['views'], cat_data['likes'])
        for p in cat_data['pages']:
            add_page(c, p['title'], p['url'])

# Print out the categories we have added.
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print(f'- {c}: {p}')

def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url=url
    p.views=views
    p.save()
    return p

def add_cat(name, views, likes):
    c = Category.objects.get_or_create(name=name,views=0,likes=0)[0]
    c.save()
    return c

# Start the program execution here:
if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()

# NOTES :
### __name__ and __main__
# The __name__ == '__main__' trick is a useful one that allows a Python module
# to act as either a reusable module or a standalone Python script. Consider
# a reusable module as one that can be imported into other modules (e.g.
# through an import statement), while a standalone Python script would be
# executed from a terminal/Command Prompt by entering python module.py.
# Code within a conditional if __name__ == '__main__' statement will therefore
# only be executed when the module is run as a standalone Python script.
# Importing the module will not run this code; any classes or functions will
# however be fully accessible to you.
### Importing Models
# When importing Django models, make sure you have imported your
# project’s settings by importing django and setting the environment variable
# DJANGO_SETTINGS_MODULE to be your project’s setting file, as demonstrated
# in lines 1 to 6 above. You then call django.setup() to import your Django
# project’s settings.
# If you don’t perform this crucial step, you’ll get an exception when attempting
# to import your models. This is because the necessary Django
# infrastructure has not yet been initialised. This is why we import Category
# and Page after the settings have been loaded on the seventh line.
