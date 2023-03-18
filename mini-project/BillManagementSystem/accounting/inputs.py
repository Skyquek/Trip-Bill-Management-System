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
    
@strawberry.input
class BillInput:
    title: str
    category_id: int
    user_id: int
    amount: decimal.Decimal
    note: str
    
@strawberry.input
class IndividualSpendingInput:
    bill_id: int
    user_id: int
    amount: decimal.Decimal
    note: str
    title: str


    
    