from strawberry.annotation import StrawberryAnnotation
from strawberry.field import StrawberryField
from typing import (
    Optional,
    
)

userid_field = StrawberryField(
    python_name="id",
    default=None,
    type_annotation=StrawberryAnnotation(int)
)
email_field = StrawberryField(
    python_name="email", 
    default=None, 
    type_annotation=StrawberryAnnotation(str)
)
username_field = StrawberryField(
    python_name="username", 
    default=None, 
    type_annotation=StrawberryAnnotation(str)
)
first_name_field = StrawberryField(
    python_name="first_name",
    default=None,
    type_annotation=StrawberryAnnotation(Optional[str]),
)
phone_number_field = StrawberryField(
    python_name="phone_number",
    default=None,
    type_annotation=StrawberryAnnotation(Optional[str]),
)
user_birthday_field = StrawberryField(
    python_name="user_birthday",
    default=None,
    type_annotation=StrawberryAnnotation(Optional[str]),
)

__all__ = [
    "userid_field",
    "email_field",
    "username_field",
    "first_name_field",
    "phone_number_field",
    "user_birthday_field"
]


