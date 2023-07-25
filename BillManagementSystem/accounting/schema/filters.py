import strawberry
from strawberry import auto, ID
from .. import models
from django.db.models import Q
import decimal
from typing import Optional

@strawberry.django.filters.filter(models.AccountUser)
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
    id: Optional[ID]
    title: auto
    note: auto
    amount: Optional[decimal.Decimal]
    amount_gte: Optional[decimal.Decimal]
    amount_lte: Optional[decimal.Decimal]
    category: Optional[int]
    user: Optional[int]
    
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

@strawberry.django.filters.filter(models.IndividualSpending)
class IndividualSpendingFilter:
    id: ID
    title: auto
    note: auto
    amount: Optional[decimal.Decimal]
    amount_gte: Optional[decimal.Decimal]
    amount_lte: Optional[decimal.Decimal]
    user: auto
    bill: Optional["BillFilter"]
    
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

@strawberry.django.filters.filter(models.Category)
class CategoryFilter:
    id: ID
    name: auto
    
    def filter_name(self, queryset):
        return queryset.filter(name__icontains=self.name)