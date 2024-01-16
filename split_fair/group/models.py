from django.db import models
import uuid 
from django.utils.translation import gettext_lazy as _

class Group(models.Model):
    class GroupType(models.TextChoices):
        TRIP = 'TR', _('Trip')
        HOME = 'HOME', _('Home')
        COUPLE = 'COUP', _('Couple')
        OTHERS = 'OTHERS', _('Others') 
                
    
    group_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    group_picture= models.ImageField(upload_to='assets/group')
    group_type = models.CharField(
        max_length = 6,
        choices=GroupType,
        default=GroupType.TRIP
    )
