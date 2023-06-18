from django.contrib import admin
from .models import Bill, Category, IndividualSpending

# Register your models here.
admin.site.register(Bill)
admin.site.register(Category)
admin.site.register(IndividualSpending)
