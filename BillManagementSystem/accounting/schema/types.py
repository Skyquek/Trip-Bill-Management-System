import strawberry
from strawberry import auto, ID
import strawberry_django
from typing import List, Union
from datetime import date
from .. import models
from django.contrib.auth.models import User as DJangoUser
import decimal


@strawberry.django.type(models.IndividualSpending)
class IndividualSpendingScalar:
    id: ID
    user: "User"
    amount: decimal.Decimal
    note: auto
    title: auto
    bill: "Bill"


@strawberry.django.type(models.Bill)
class Bill:
    id: ID
    title: str
    note: str
    amount: str
    category: "Category"
    user: "User"

    @strawberry.field
    def individual_spendings(self) -> List[IndividualSpendingScalar]:
        return models.IndividualSpending.objects.filter(bill_id=self.id)


@strawberry.django.type(models.Category)
class Category:
    id: int
    name: str
    bills: List[Bill]


@strawberry.django.type(DJangoUser)
class DJangoUser:
    username: auto
    first_name: auto
    last_name: auto
    email: auto


@strawberry.django.type(models.User)
class User:
    id: strawberry.ID
    birthday: date
    phone_number: str
    # Issue: https://github.com/strawberry-graphql/strawberry-graphql-django/issues/245
    django_user: DJangoUser = strawberry_django.field(field_name="user") 

    @strawberry.field
    def bills(self) -> List[Bill]:
        return models.Bill.objects.filter(user=self.id)

    @strawberry.field
    def individual_spendings(self) -> List[IndividualSpendingScalar]:
        return models.IndividualSpending.objects.filter(user=self.id)


@strawberry.type
class AuthResponse:
    success: bool
    token: str = ""
    user: Union[User, None]
    error: str = ""


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
        bills=models.Bill.objects.filter(user=user["id"]),
        individual_spendings=models.IndividualSpending.objects.filter(
            user=user["id"])
    )
    return user
