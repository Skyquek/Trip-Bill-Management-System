import strawberry
from typing import List
from .types import Bill

@strawberry.type
class Query:
    bills: List[Bill] = strawberry.django.field()
    
schema = strawberry.Schema(query=Query)