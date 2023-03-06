import strawberry
from typing import List
from .types import Bill, IndividualSpending, Category, User, AdminUser
from strawberry_django import mutations
from .inputs import UserInput, AdminInput, CategoryInput, BillInput, IndividualSpendingInput

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
    createCategory: Category = mutations.create(CategoryInput)
    createBill: Bill = mutations.create(BillInput)
    createIndividualSpending: IndividualSpending = mutations.create(IndividualSpendingInput)
    
schema = strawberry.Schema(query=Query, mutation=Mutation)