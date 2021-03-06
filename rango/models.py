from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    NAME_MAX_LENGTH = 128

    name = models.CharField(max_length=NAME_MAX_LENGTH, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)
    # if unique, attribute field in db must always be unique
    # in the e.g. it's the field 'name' which must be unique in the db
    # if unique, the name field can also be used as a primary key

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

class Page(models.Model):
    TITLE_MAX_LENGTH = 128
    URL_MAX_LENGTH = 200

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # category is a ForeignKey, with a 1 to Many relationship
    # CASCADE instructs Django to delete the pages associated with the
    # category when the category is deleted
    title = models.CharField(max_length=TITLE_MAX_LENGTH) # stores chars
    url = models.URLField() # stores resource URLs
    views = models.IntegerField(default=0) # stores integers

    def __str__(self):
        return self.title
    # def a str method which alters what is shown when category is printed
    # instead of <Category: Category object> it will now show <Category: title>
    # equivalent to java's toString method

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username
