import datetime
from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
      
    def __str__(self):
        return str(self.question_text)
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=100)
    
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self) -> str:
        return str(self.choice_text)
    
class Author(models.Model):
    author = models.ForeignKey(Question, on_delete=models.CASCADE)
    author_name = models.CharField(max_length=200)
    
    def __str__(self) -> str:
        return str(self.author_name)
    