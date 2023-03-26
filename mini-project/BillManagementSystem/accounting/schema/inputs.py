import strawberry
from strawberry import auto, ID
from typing import List, Optional
from .. import models
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
    
# @strawberry.django.input(models.User)
# class RegisterInput:
#     username: str
#     first_name: str
#     last_name: str
#     email: str
#     password: str
#     birthday: auto
#     phone_number: str
    
@strawberry.django.input(models.Category)
class CategoryInput:
    name: str

@strawberry.django.input(models.Category, partial=True)
class CategoryPartialInput(CategoryInput):
    id: ID
    name: auto

@strawberry.django.input(models.Bill)
class BillInput:
    title: str
    category_id: int # How to make this optional
    user_id: int # How to make this optional
    amount: decimal.Decimal
    note: str
    
@strawberry.django.input(models.Bill, partial=True)
class BillPartialInput(BillInput):
    id: ID
    title: auto
    category_id: int
    user_id: int
    amount: decimal.Decimal
    note: auto
    
@strawberry.django.input(models.IndividualSpending)
class IndividualSpendingInput:
    bill_id: int
    user_id: int
    amount: decimal.Decimal
    note: str
    title: str

@strawberry.django.input(models.IndividualSpending, partial=True)
class IndividualSpendingPartialInput(IndividualSpendingInput):
    id: ID
    user_id: int
    amount: decimal.Decimal
    note: auto
    title: auto
    
    
