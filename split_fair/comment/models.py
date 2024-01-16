from django.db import models
from django.contrib.auth.models import User
import uuid

class Comment(models.Model):
    comment_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment_user_id')
    expense_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment_expense_id')
    text = models.TextField()

