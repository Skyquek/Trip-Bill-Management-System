import strawberry
from typing import List
from .types import Bill, IndividualSpending, Category, User, AdminUser
from strawberry_django import mutations
from .inputs import UserInput, AdminInput

@strawberry.type
class Query:
    bills: List[Bill] = strawberry.django.field()
    individual_spendings: List[IndividualSpending] = strawberry.django.field()
    categories: List[Category] = strawberry.django.field()
    users: List[User] = strawberry.django.field()
    
@strawberry.type
class Mutation:
    createAdmin: AdminUser = mutations.create(AdminInput)
    createUser: User = mutations.create(UserInput)
    
schema = strawberry.Schema(query=Query, mutation=Mutation)