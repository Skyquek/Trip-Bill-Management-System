import strawberry
from strawberry import auto
from typing import List, Union
from datetime import date
from . import models

def get_category_for_bill(root) -> "Category":
    return Category(
        id=1,
        name="Food"
    )
    
def get_bills_for_category(root):
    return [
        Bill(
            id=1,
            user_id=1,
            title="Skypark Dinner",
            amount=100,
            note="bleh!"
        )
    ]
    
@strawberry.django.type(models.IndividualSpending)
class IndividualSpending:
    id: auto
    bill: auto
    user: 'User'
    amount: str
    note: auto
    title: auto
    
@strawberry.type
class Bill:
    id: int
    user_id: int
    title: str
    category: "Category" = strawberry.field(resolver=get_category_for_bill)
    amount: str
    note: str
    
@strawberry.type
class Category:
    id: int
    name: str
    bills: List[Bill] = strawberry.field(resolver=get_bills_for_category)
    
    
@strawberry.type
class User:
    id: int
    username: str
    first_name: str
    last_name: str
    email: str
    birthday: date
    phone_number: str
    bills: Union[List[Bill], None]
    individual_spendings: Union[List[Bill], None]
    
