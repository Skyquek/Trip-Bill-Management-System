from djmoney.models.fields import MoneyField
from phonenumber_field.modelfields import PhoneNumberField
from model_utils.models import TimeStampedModel

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class User(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthday = models.DateField()
    phone_number = PhoneNumberField(blank=True)
    
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
class Bill(TimeStampedModel):
    title = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = MoneyField(max_digits=19, decimal_places=2, default_currency='MYR')
    note = models.TextField()
    
class IndividualSpending(TimeStampedModel):
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = MoneyField(max_digits=19, decimal_places=2, default_currency='MYR')
    note = models.TextField()
    
class Debt(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = MoneyField(max_digits=19, decimal_places=2, default_currency='MYR')
    



