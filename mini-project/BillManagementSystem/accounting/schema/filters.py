import strawberry
from strawberry import auto, ID
from .. import models
from django.db.models import Q
import decimal

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
    
@strawberry.django.filters.filter(models.Bill)
class BillFilter:
    id: ID
    title: auto
    note: auto
    amount: decimal.Decimal
    amount_gte: decimal.Decimal
    amount_lte: decimal.Decimal
    category: int
    user: int
    
    def filter_title(self, queryset):
        return queryset.filter(title__icontains=self.title)
    
    def filter_note(self, queryset):
        return queryset.filter(note__icontains=self.note)
    
    def filter_amount(self, queryset):
        return queryset.filter(amount__exact=self.amount)
    
    def filter_amount_gte(self, queryset):
        return queryset.filter(amount__gte=self.amount_gte)
    
    def filter_amount_lte(self, queryset):
        return queryset.filter(amount__lte=self.amount_lte)
    
    