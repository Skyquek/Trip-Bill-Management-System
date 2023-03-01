from django.contrib import admin
from .models import Bill, User, Category

# Register your models here.
admin.site.register(Bill)
admin.site.register(User)
admin.site.register(Category)
