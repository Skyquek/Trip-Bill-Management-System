import strawberry
from strawberry import auto
from typing import List
from . import models
from django.contrib.auth.models import User as AdminUser
import decimal

@strawberry.django.input(AdminUser)
class AdminInput:
    username: str
    password: str
    
@strawberry.django.input(models.User)
class UserInput:
    id: auto
    birthday: auto
    phone_number: str
    user: str
    
@strawberry.django.input(models.Category)
class CategoryInput:
    id: auto
    name: auto
    
@strawberry.django.input(models.Bill)
class BillInput:
    id: auto
    user_id: int
    title: auto
    category: int
    amount: decimal.Decimal
    note: auto
    
@strawberry.django.input(models.IndividualSpending)
class IndividualSpendingInput:
    id: auto
    bill: int
    user: int
    amount: decimal.Decimal
    note: str
    title: str
    
    
    