import strawberry
from typing import List
from django.contrib.auth.models import User as AdminUser
from .inputs import CategoryInput, CategoryPartialInput, RegisterInput, BillInput, BillPartialInput, IndividualSpendingInput, IndividualSpendingPartialInput
from strawberry_django import mutations
from .. import models
from django.contrib.auth.tokens import default_token_generator

from .types import IndividualSpending, Bill, Category, User, AuthResponse
from .filters import UserFilter, BillFilter, IndividualSpendingFilter, CategoryFilter

@strawberry.type
class Query:
    categories: List[Category] = strawberry.django.field()
    category: List[Category] = strawberry.django.field(filters=CategoryFilter)
    
    users: List[User] = strawberry.django.field()
    user: List[User] = strawberry.django.field(filters=UserFilter)

    bills: List[Bill] = strawberry.django.field()
    bill: List[Bill] = strawberry.django.field(filters=BillFilter)
    
    individualSpendings: List[IndividualSpending] = strawberry.django.field()
    individualSpending: List[IndividualSpending] = strawberry.django.field(filters=IndividualSpendingFilter)
    
@strawberry.type
class Mutation:
    # createUser: User = mutations.create(RegisterInput)
    
    # TODO: How to change this to strawberry style
    # There is one bug on one to one relationship
    # https://github.com/strawberry-graphql/strawberry-graphql-django/issues/235     
    @strawberry.mutation
    def add_user(self, register_input: RegisterInput) -> AuthResponse:
        django_user = AdminUser.objects.create_user(
            username=register_input.username, 
            email=register_input.email, 
            password=register_input.password, 
            first_name=register_input.first_name, 
            last_name = register_input.last_name
        )

        accounting_user = models.User(user=django_user, birthday=register_input.birthday, phone_number=register_input.phone_number)
        accounting_user.save()
        
        new_user = User(
            id=accounting_user.id,
            birthday=accounting_user.birthday,
            phone_number=accounting_user.phone_number,
            django_user = django_user
        )
        token = default_token_generator.make_token(django_user)
        
        return AuthResponse(success=True, token=token, user=new_user)
    
    # create
    # createUser: User = mutations.create(RegisterInput)
    createCategory: Category = mutations.create(CategoryInput)
    createBill: Bill = mutations.create(BillInput)
    createIndividualSpending: IndividualSpending = mutations.create(IndividualSpendingInput)
    
    # update
    updateCategory: List[Category] = mutations.update(CategoryPartialInput, filters=CategoryFilter)
    updateBill: List[Bill] = mutations.update(BillPartialInput, filters=BillFilter)
    updateIndividualSpending: List[IndividualSpending] = mutations.update(IndividualSpendingPartialInput, filters=IndividualSpendingFilter)
    
    # delete
    
    # TODO:this is dangerous, they can feed in deletion all without filter
    deleteCategory: List[Category] = mutations.delete(filters=CategoryFilter)
    deleteBill: List[Bill] = mutations.delete(filters=BillFilter)
    deleteIndividualSpending: List[IndividualSpending] = mutations.delete(filters=IndividualSpendingFilter)
    
        
schema = strawberry.Schema(query=Query, mutation=Mutation)