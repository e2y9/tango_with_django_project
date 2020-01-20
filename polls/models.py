import datetime

from django.db import models
from django.utils import timezone
# Each model is represented by a class that subclasses django.db.models.Model
# Each model has a number of class variables, each of which represents a
# database field in the model.

# Each field is represented by an instance of a Field class – e.g., CharField
# for character fields and DateTimeField for datetimes. This tells Django what
# type of data each field holds.

class Question(models.Model):
    question_text = models.CharField(max_length=200) # CharField must def len
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
        # returns a boolean if pub date is recent


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # ForeignKey tells Django each Choice is related to a single Question.
    # Django supports all the common database relationships: many-to-one,
    # many-to-many, and one-to-one.
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0) # default num votes = 0

    def __str__(self):
        return self.choice_text
