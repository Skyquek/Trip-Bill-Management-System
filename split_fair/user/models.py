from django.db import models
from django.contrib.auth.models import User
import uuid

class Profile(models.Model):
    profile_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    currency = models.CharField(max_length=5, default='MYR')
    language = models.CharField(max_length=200, )
    profile_picture = models.ImageField(upload_to='assets/profile_picture')
    
class Friendship(models.Model):
    friendship_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friendship_user_1')
    user2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friendship_user_2')
    

