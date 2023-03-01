import strawberry
from typing import List
from .types import Bill, IndividualSpending, Category, User

@strawberry.type
class Query:
    bills: List[Bill] = strawberry.django.field()
    individual_spendings: List[IndividualSpending] = strawberry.django.field()
    categories: List[Category] = strawberry.django.field()
    users: List[User] = strawberry.django.field()
    
schema = strawberry.Schema(query=Query)