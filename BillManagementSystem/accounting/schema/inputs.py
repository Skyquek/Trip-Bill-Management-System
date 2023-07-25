import strawberry
from strawberry import auto, ID
from typing import List, Optional
from .. import models
import decimal
from datetime import date

from django.contrib.auth import get_user_model
    
@strawberry.django.input(models.AccountUser)
class RegisterInput:
    username: str
    first_name: str
    last_name: str
    email: str
    password: str
    birthday: date
    phone_number: str
    
@strawberry.django.input(get_user_model())
class UserLoginInput:
    username: auto
    password: auto
    
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
    category: Optional[int]
    user: Optional[int]
    amount: decimal.Decimal
    note: str
    
@strawberry.django.input(models.Bill, partial=True)
class BillPartialInput(BillInput):
    id: ID
    title: auto
    category_id: auto
    user_id: auto
    amount: Optional[decimal.Decimal]
    note: auto
    
@strawberry.django.input(models.IndividualSpending)
class IndividualSpendingInput:
    bill: auto
    user: auto
    amount: Optional[decimal.Decimal]
    note: auto
    title: auto

@strawberry.django.input(models.IndividualSpending, partial=True)
class IndividualSpendingPartialInput(IndividualSpendingInput):
    id: ID
    user: auto
    amount: Optional[decimal.Decimal]
    note: auto
    title: auto
    
    
