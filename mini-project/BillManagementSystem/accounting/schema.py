import strawberry
from django.db import IntegrityError
from typing import List, Optional, Union
from django.contrib.auth.models import User as AdminUser
from .inputs import CategoryInput, RegisterInput
# from strawberry_django import mutations
from . import models
from strawberry import auto
from django.core.exceptions import ValidationError
from django.contrib.auth.tokens import default_token_generator
from datetime import date

from .types import IndividualSpending, Bill, Category, User

def get_categories(root) -> List[Bill]:
    return [
        Category(
            id=1,
            name="Food"
        ),
        Category(
            id=2,
            name="Parking"
        )
    ]
    
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
            print(bill)
            
        if title:
            bill = queryset.filter(title__icontains=title)
            
        if category_id:
            category = models.Category.objects.get(id=category_id)
            bill = queryset.filter(category=category)
            
        return bill

@strawberry.type
class Query:
    bill: List[Bill] = strawberry.field(resolver=get_bills_by_filter)
    categories: List[Category] = strawberry.field(resolver=get_categories)
    # individual_spendings: List[IndividualSpending] = strawberry.django.field()
    # users: List[User] = strawberry.django.field()

################################ Mutation Function ##############################
@strawberry.type
class CategoryResponse:
    success: bool
    category: Category = ""
    error: str = ""
    
@strawberry.type
class AuthResponse:
    success: bool
    token: str = ""
    user: Union[User, None]
    error: str = ""

@strawberry.type
class Mutation:
    
    @strawberry.mutation
    def add_user(self, register_input: RegisterInput) -> AuthResponse:
        try:
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
        except IntegrityError as e:
            return AuthResponse(success=False, user=None, error="This username is taken. Please choose others!")
        except ValidationError as e:
            return AuthResponse(success=False, user=None, error=str(e))
    
    @strawberry.mutation
    def add_category(self, category: CategoryInput) -> CategoryResponse:
        category = models.Category(name=category.name)
        try:
            category.save()
            return CategoryResponse(success=True, category=category)
        except IntegrityError as e:
            return CategoryResponse(success=False, error="This category is taken. Don't create similar category!")
        except ValidationError as e:
            return CategoryResponse(success=False, error=str(e))

schema = strawberry.Schema(query=Query, mutation=Mutation)