import strawberry
from strawberry import auto
from typing import List
from . import models
import decimal
from datetime import date
    
@strawberry.input
class RegisterInput:
    username: str
    first_name: str
    last_name: str
    email: str
    password: str
    birthday: date
    phone_number: str
    
@strawberry.django.input(models.Category)
class CategoryInput:
    name: str
    
@strawberry.django.input(models.IndividualSpending)
class IndividualSpendingInput:
    id: auto
    bill: int
    user: int
    amount: decimal.Decimal
    note: str
    title: str
    
    
    