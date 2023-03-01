from django.contrib import admin
from .models import Bill, User, Category, IndividualSpending

# Register your models here.
admin.site.register(Bill)
admin.site.register(User)
admin.site.register(Category)
admin.site.register(IndividualSpending)
