import strawberry
from strawberry import auto
from typing import List, Union
from datetime import date
from .. import models
    
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
    bill: "Bill"
    user: "User"
    amount: str
    note: auto
    title: auto
    
@strawberry.type
class Bill:
    id: int
    user: "User"
    title: str
    category: "Category"
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
    
@strawberry.type
class IndividualSpendingResponse:
    success: bool
    individual_spending: Union[IndividualSpending, None]
    error: str = ""

@strawberry.type
class BillResponse:
    success: bool
    bill: Union[Bill, None]
    error: str = ""
    
@strawberry.type
class AuthResponse:
    success: bool
    token: str = ""
    user: Union[User, None]
    error: str = ""
    
@strawberry.type
class CategoryResponse:
    success: bool
    category: Union[Category, None]
    error: str = ""
    
@strawberry.type
class UserResponse:
    success: bool
    user: User | None | List[User]
    
def get_user_all_details(user_id: int):
    user = models.User.objects.select_related("user").filter(id=2).values(
        "id", 
        "user__username",
        "user__first_name",
        "user__last_name",
        "user__email",
        "birthday",
        "phone_number",
    ).get()
    
                
    if not user["user__first_name"]:
        user["user__first_name"] = ""
    
    if not user["user__last_name"]:
        user["user__last_name"] = ""
        
    print(user)

    user = User(
        id=user["id"], 
        username=user["user__username"],
        first_name=user["user__first_name"],
        last_name=user["user__last_name"],
        email=user["user__email"],
        birthday=user["birthday"],
        phone_number=user["phone_number"],
        bills = models.Bill.objects.filter(user=user["id"]),
        individual_spendings = models.IndividualSpending.objects.filter(user=user["id"])
    )    
    return user
    