import strawberry
from typing import List
from django.contrib.auth.models import User as AdminUser
from .inputs import CategoryInput, CategoryPartialInput, RegisterInput, BillInput, BillPartialInput, IndividualSpendingInput, IndividualSpendingPartialInput
from strawberry_django import mutations
from .. import models
from django.contrib.auth.tokens import default_token_generator

from .types import IndividualSpendingScalar, BillScalar, CategoryScalar, UserScalar, AuthResponse
from .filters import UserFilter, BillFilter, IndividualSpendingFilter, CategoryFilter

@strawberry.type
class Query:
    categories: List[CategoryScalar] = strawberry.django.field()
    category: List[CategoryScalar] = strawberry.django.field(filters=CategoryFilter)
    
    users: List[UserScalar] = strawberry.django.field()
    user: List[UserScalar] = strawberry.django.field(filters=UserFilter)

    bills: List[BillScalar] = strawberry.django.field()
    bill: List[BillScalar] = strawberry.django.field(filters=BillFilter)
    
    individualSpendings: List[IndividualSpendingScalar] = strawberry.django.field()
    individualSpending: List[IndividualSpendingScalar] = strawberry.django.field(filters=IndividualSpendingFilter)
    
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

        accounting_user = models.User.objects.create(
            user=django_user, 
            birthday=register_input.birthday, 
            phone_number=register_input.phone_number
        )
        
        new_user = UserScalar(
            id=accounting_user.id,
            birthday=accounting_user.birthday,
            phone_number=accounting_user.phone_number,
            django_user = django_user
        )
        token = default_token_generator.make_token(django_user)
        
        return AuthResponse(success=True, token=token, user=new_user)
    
    # create
    # createUser: User = mutations.create(RegisterInput)
    createCategory: CategoryScalar = mutations.create(CategoryInput)
    createBill: BillScalar = mutations.create(BillInput)
    createIndividualSpending: IndividualSpendingScalar = mutations.create(IndividualSpendingInput)
    
    # update
    updateCategory: List[CategoryScalar] = mutations.update(CategoryPartialInput, filters=CategoryFilter)
    updateBill: List[BillScalar] = mutations.update(BillPartialInput, filters=BillFilter)
    updateIndividualSpending: List[IndividualSpendingScalar] = mutations.update(IndividualSpendingPartialInput, filters=IndividualSpendingFilter)
    
    # delete
    
    # TODO:this is dangerous, they can feed in deletion all without filter
    deleteCategory: List[CategoryScalar] = mutations.delete(filters=CategoryFilter)
    deleteBill: List[BillScalar] = mutations.delete(filters=BillFilter)
    deleteIndividualSpending: List[IndividualSpendingScalar] = mutations.delete(filters=IndividualSpendingFilter)
    
        
schema = strawberry.Schema(query=Query, mutation=Mutation)