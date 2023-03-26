import strawberry
from strawberry import auto
import strawberry_django
from typing import List, Union
from datetime import date
from .. import models
from django.contrib.auth.models import User as DJangoUser
    
@strawberry.django.type(models.IndividualSpending)
class IndividualSpending:
    id: auto
    bill: "Bill"
    user: "User"
    amount: str
    note: auto
    title: auto
    
@strawberry.django.type(models.Bill)
class Bill:
    id: int
    title: str
    note: str
    amount: str
    category: "Category"
    user: "UserOutput"

    
@strawberry.type
class Category:
    id: int
    name: str
    bills: List[Bill]
    
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
    
@strawberry.django.type(models.User)
class UserOutput:
    id: strawberry.ID
    username: str
    birthday: date
    phone_number: str
    
    @strawberry.field
    def first_name(self) -> str:
        return self.user.first_name
    
    @strawberry.field
    def last_name(self) -> str:
        return self.user.last_name
    
    @strawberry.field
    def email(self) -> str:
        return self.user.email
    
    @strawberry.field
    def bills(self) -> List[Bill]:
        return models.Bill.objects.filter(user=self.id)
    
    @strawberry.field
    def individual_spendings(self) -> List[IndividualSpending]:
        return models.IndividualSpending.objects.filter(user=self.id)
        
    
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
    