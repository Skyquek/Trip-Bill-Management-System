import strawberry
from django.db import IntegrityError
from typing import List, Optional, Union
from django.contrib.auth.models import User as AdminUser
from .inputs import CategoryInput, RegisterInput, BillInput, IndividualSpendingInput
# from strawberry_django import mutations
from .. import models
from strawberry import auto
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.contrib.auth.tokens import default_token_generator
from datetime import date
from django.db.models import F

from .types import IndividualSpending, Bill, Category, User, IndividualSpendingResponse, get_user_all_details, CategoryResponse, AuthResponse, UserResponse

# Category
def get_all_categories(root) -> List[Category]:
    return models.Category.objects.all()

def get_category_by_id(self, id: int) -> CategoryResponse:
    try:
        category = models.Category.objects.get(id=id)
        return CategoryResponse(
            success=True,
            category=category
        )
    except models.Category.DoesNotExist as e:
        return CategoryResponse(
            success=False,
            category= None,
            error='Bro, this category Does not Exist!'
        )    

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

# user
def get_user_by_id(self, id: int) -> UserResponse:
    try:
        user : models.User = models.User.objects.get(id=id)
        return User(
            id=id,
            username=user.user.username
        )
    except models.User.DoesNotExist as e:
        return 
    
# Bill    
def get_bills_by_filter(self, 
                        id: Optional[int] = None, 
                        user_id: Optional[int] = None, 
                        title: Optional[str] = None, 
                        category_id: Optional[int] = None) -> Bill:
    
    if not any((id, user_id, title, category_id)):
        raise ValueError("Hey! Please query by at least one parameter!")
    
    if id is not None:
        bill = models.Bill.objects.get(id=id)
        return [bill]
    else:
        queryset = models.Bill.objects.all()
        
        if user_id:
            user = models.User.objects.get(id=user_id)
            bill = queryset.filter(user=user)
            
        if title:
            bill = queryset.filter(title__icontains=title)
            
        if category_id:
            category = models.Category.objects.get(id=category_id)
            bill = queryset.filter(category=category)
            
        return bill

@strawberry.type
class Query:
    category: CategoryResponse = strawberry.field(resolver=get_category_by_id)
    categories: List[Category] = strawberry.field(resolver=get_all_categories)
    user: List[User] = strawberry.field(resolver=get_all_users)
    bill: List[Bill] = strawberry.field(resolver=get_bills_by_filter)

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