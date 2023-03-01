import strawberry
from strawberry import auto
from typing import List
from . import models
    
@strawberry.django.type(models.Bill)
class Bill:
    id: auto
    user_id: auto
    title: auto
    category: "Category"
    amount: str
    note: auto
    
@strawberry.django.type(models.IndividualSpending)
class IndividualSpending:
    id: auto
    bill: auto
    user: 'User'
    amount: str
    note: auto
    title: auto
    
@strawberry.django.type(models.Category)
class Category:
    id: auto
    name: auto
    bills: List[Bill]
    
@strawberry.django.type(models.User)
class User:
    id: auto
    birthday: auto
    phone_number: str
    bills: List[Bill]
    individual_spendings: List[Bill]
    