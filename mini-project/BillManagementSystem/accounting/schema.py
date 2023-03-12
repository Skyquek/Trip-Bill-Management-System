import strawberry
from typing import List, Optional
from .types import AdminUser
# from strawberry_django import mutations
from . import models
from strawberry import auto

# from .inputs import UserInput, AdminInput, CategoryInput, IndividualSpendingInput

@strawberry.django.type(models.IndividualSpending)
class IndividualSpending:
    id: auto
    bill: auto
    user: 'User'
    amount: str
    note: auto
    title: auto
    
@strawberry.django.type(AdminUser)
class AdminUser:
    id: int
    username: str
    password: auto
    email: str
    
#####################################################
def get_category_for_bill(root) -> "Category":
    return Category(
        id=1,
        name="Food"
    )

@strawberry.type
class Bill:
    id: int
    user_id: int
    title: str
    category: "Category" = strawberry.field(resolver=get_category_for_bill)
    amount: str
    note: str
    
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

@strawberry.type
class Category:
    id: int
    name: str
    bills: List[Bill] = strawberry.field(resolver=get_bills_for_category)

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
    
@strawberry.django.type(models.User)
class User:
    id: auto
    birthday: auto
    phone_number: str
    user: str
    bills: List[Bill]
    individual_spendings: List[Bill]

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
    
# @strawberry.type
# class Mutation:
#     createAdmin: AdminUser = mutations.create(AdminInput)
#     createUser: User = mutations.create(UserInput)
#     createCategory: Category = mutations.create(CategoryInput)
#     # createBill: Bill = mutations.create(BillInput)
#     createIndividualSpending: IndividualSpending = mutations.create(IndividualSpendingInput)
    
schema = strawberry.Schema(query=Query)