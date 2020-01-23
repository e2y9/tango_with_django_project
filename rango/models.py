from django.db import models
from django.template.defaultfilters import slugify

class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
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
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Page(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # category is a ForeignKey, with a 1 to Many relationship
    # CASCADE instructs Django to delete the pages associated with the
    # category when the category is deleted
    title = models.CharField(max_length=128) # stores chars
    url = models.URLField() # stores resource URLs
    views = models.IntegerField(default=0) # stores integers

    def __str__(self):
        return self.title
    # def a str method which alters what is shown when category is printed
    # instead of <Category: Category object> it will now show <Category: title>
    # equivalent to java's toString method
