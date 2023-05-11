from djmoney.models.fields import MoneyField
from phonenumber_field.modelfields import PhoneNumberField
from model_utils.models import TimeStampedModel

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class AccountUser(AbstractUser):
    email = models.EmailField(
        blank=False, 
        max_length=254, 
        verbose_name="email address"
    )
    user_birthday = models.DateField(null=True)
    phone_number = PhoneNumberField(blank=True)
    
    USERNAME_FIELD = "username"   # e.g: "username", "email"
    EMAIL_FIELD = "email"         # e.g: "email", "primary_email"
    
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
class Bill(TimeStampedModel):
    title = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(AccountUser, on_delete=models.CASCADE)
    amount = MoneyField(max_digits=19, decimal_places=2, default_currency='MYR')
    note = models.TextField()
    
class IndividualSpending(TimeStampedModel):
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE)
    user = models.ForeignKey(AccountUser, on_delete=models.CASCADE)
    amount = MoneyField(max_digits=19, decimal_places=2, default_currency='MYR')
    note = models.TextField()
    title = models.CharField(max_length=50)