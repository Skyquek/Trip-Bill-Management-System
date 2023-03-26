import strawberry
from django.db import IntegrityError
from typing import List, Optional, Union
from django.contrib.auth.models import User as AdminUser
from .inputs import CategoryInput, RegisterInput, BillInput, IndividualSpendingInput
from strawberry_django import mutations
from .. import models
from strawberry import auto
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.contrib.auth.tokens import default_token_generator
from datetime import date
from django.db.models import F

from .types import IndividualSpending, Bill, Category, User, IndividualSpendingResponse, get_user_all_details, CategoryResponse, AuthResponse, UserResponse, UserOutput
from .filters import UserFilter, BillFilter, IndividualSpendingFilter, CategoryFilter

# User
def get_all_users(root) -> List[User]:
    users = models.User.objects.all()
    users_list = list()
    for user in users:
        users_list.append(
            User(
            id=user.id,
            username=user.user.username,
            first_name=user.user.first_name,
            last_name=user.user.last_name,
            email=user.user.email,
            birthday=user.birthday,
            phone_number=user.phone_number,
            bills = models.Bill.objects.filter(user=user.id),
            individual_spendings = models.IndividualSpending.objects.filter(user=user.id)
        )
    )  
    
    return users_list

@strawberry.type
class Query:
    categories: List[Category] = strawberry.django.field()
    category: List[Category] = strawberry.django.field(filters=CategoryFilter)
    
    users: List[User] = strawberry.field(resolver=get_all_users)
    user: List[UserOutput] = strawberry.django.field(filters=UserFilter)

    bills: List[Bill] = strawberry.django.field()
    bill: List[Bill] = strawberry.django.field(filters=BillFilter)
    
    individualSpendings: List[IndividualSpending] = strawberry.django.field()
    individualSpending: List[IndividualSpending] = strawberry.django.field(filters=IndividualSpendingFilter)
    

@strawberry.type
class Mutation:
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
            username=django_user.username,
            first_name=django_user.first_name,
            last_name=django_user.last_name,
            email=django_user.email,
            birthday=accounting_user.birthday,
            phone_number=accounting_user.phone_number,
            bills= None,
            individual_spendings=None
        )
        token = default_token_generator.make_token(django_user)
        
        return AuthResponse(success=True, token=token, user=new_user)
    
    @strawberry.mutation
    def add_category(self, category: CategoryInput) -> CategoryResponse:
        category = models.Category(name=category.name)
        try:
            category.save()
            return CategoryResponse(success=True, category=category)
        except IntegrityError as e:
            return CategoryResponse(success=False, category=None, error="This category is taken. Don't create similar category!") 
        except ValidationError as e:
            return CategoryResponse(success=False, category=None, error=str(e))
        
    @strawberry.mutation
    def add_bill(self, bill: BillInput) -> Bill:
        category = models.Category.objects.get(id=bill.category_id)
        biller = models.User.objects.get(id=bill.user_id)
        
        bill = models.Bill(title=bill.title, category=category, user=biller, amount=bill.amount, note=bill.note)
        bill.save()
                
        bill_res = Bill(
            id=bill.id, 
            user=get_user_all_details(bill.user_id), 
            title=bill.title, 
            category=category, 
            amount=bill.amount, 
            note=bill.note
        )
        
        return bill_res

    @strawberry.mutation
    def add_individual_spending(self, spending: IndividualSpendingInput) -> IndividualSpendingResponse:
        try:
            bill = models.Bill.objects.get(id=spending.bill_id)
            individual_user_spending = models.User.objects.get(id=spending.user_id)
            
            # Save the individual spending
            spending = models.IndividualSpending(
                bill=bill, 
                user=individual_user_spending, 
                amount=spending.amount, 
                note=spending.note, 
                title=spending.title
            )
            spending.save()
            
            bill = Bill(
                id=bill.id,
                user= get_user_all_details(bill.user_id),
                title=bill.title,
                category=bill.category,
                amount = bill.amount,
                note=bill.note
            )
            
            spending = IndividualSpending(
                id = spending.id,
                bill = bill,
                user = get_user_all_details(spending.user_id),
                amount = spending.amount,
                note = spending.note,
                title = spending.title
            )
            
            return IndividualSpendingResponse(
                success=True,
                individual_spending=spending
            )
        except ValidationError as e:
            return IndividualSpendingResponse(
                success=False, 
                individual_spending=None, 
                error= str(e)
            )
            
schema = strawberry.Schema(query=Query, mutation=Mutation)