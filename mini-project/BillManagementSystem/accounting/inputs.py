import strawberry
from strawberry import auto
from typing import List
from . import models
from django.contrib.auth.models import User as AdminUser

@strawberry.django.input(AdminUser)
class AdminInput:
    username: str
    password: str
    
@strawberry.django.input(models.User)
class UserInput:
    id: auto
    birthday: auto
    phone_number: str
    user: str
    