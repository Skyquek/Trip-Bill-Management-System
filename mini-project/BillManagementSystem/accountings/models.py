from djmoney.models.fields import MoneyField
from phonenumber_field.modelfields import PhoneNumberField

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Payment(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = MoneyField(max_digits=19, decimal_places=2, default_currency='MYR')
    note = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    
class Debt(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = MoneyField(max_digits=19, decimal_places=2, default_currency='MYR')
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    
class Category(models.Model):
    name = models.TextField()
    
class Expenses(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = MoneyField(max_digits=19, decimal_places=2, default_currency='MYR')
    note = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthday = models.DateTimeField()
    email = models.EmailField()
    phone_number = PhoneNumberField(blank=True)



