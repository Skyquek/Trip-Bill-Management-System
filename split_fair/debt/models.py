from django.db import models
import uuid
from django.contrib.auth.models import User

class Debt(models.Model):
    debt_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    debtor_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='debts_as_debtor')
    creditor_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='debts_as_creditor')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
