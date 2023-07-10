import strawberry
from strawberry import auto, ID
import strawberry_django
from typing import List, Union
from datetime import date
from .. import models
from django.contrib.auth.models import User as DjangoUser
import decimal

from django.contrib.auth import get_user_model

@strawberry.django.type(models.IndividualSpending)
class IndividualSpendingScalar:
    id: ID
    user: "UserScalar"
    amount: decimal.Decimal
    note: auto
    title: auto
    bill: "BillScalar"


@strawberry.django.type(models.Bill)
class BillScalar:
    id: ID
    title: str
    note: str
    amount: str
    category: "CategoryScalar"
    user: "UserScalar"

    @strawberry.field
    def individual_spendings(self) -> List[IndividualSpendingScalar]:
        return models.IndividualSpending.objects.filter(bill_id=self.id)


@strawberry.django.type(models.Category)
class CategoryScalar:
    id: int
    name: str
    bills: List[BillScalar]

@strawberry.django.type(get_user_model())
class UserAuth:
    username: auto
    email: auto

@strawberry.django.input(get_user_model())
class UserLoginInput:
    username: auto
    password: auto

@strawberry.django.type(DjangoUser)
class DjangoUser:
    username: auto
    first_name: auto
    last_name: auto
    email: auto


@strawberry.django.type(models.AccountUser)
class UserScalar:
    id: strawberry.ID
    user_birthday: date
    phone_number: str
    # Issue: https://github.com/strawberry-graphql/strawberry-graphql-django/issues/245
    # django_user: DjangoUser = strawberry_django.field(field_name="user") 

    @strawberry.field
    def bills(self) -> List[BillScalar]:
        return models.Bill.objects.filter(user=self.id)

    @strawberry.field
    def individual_spendings(self) -> List[IndividualSpendingScalar]:
        return models.IndividualSpending.objects.filter(user=self.id)


@strawberry.type
class AuthResponse:
    success: bool
    token: str = ""
    user: Union[UserScalar, None]
    error: str = ""
