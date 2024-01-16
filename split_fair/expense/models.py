from django.db import models
import uuid
from group.models import Group

class Expense(models.Model):
    expense_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    category = models.CharField(max_length=30)
    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    receipt_image = models.ImageField(upload_to='assets/expense/receipt')
    note = models.TextField()
    
    
