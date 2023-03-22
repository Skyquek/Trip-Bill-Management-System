import strawberry
from strawberry import auto, ID
from .. import models
from django.db.models import Q

@strawberry.django.filters.filter(models.User)
class UserFilter:
    id: ID
    phone_number: str
    name_contains: str
    email: str
    
    def filter_id(self, queryset):
        return queryset.filter(id=self.id)
    
    def filter_name_contains(self, queryset):
        return queryset.filter(
            Q(user__first_name__icontains=self.name_contains) |
            Q(user__last_name__icontains=self.name_contains)
        )
    
    def filter_email(self, queryset):
        return queryset.filter(user__email__icontains=self.email)