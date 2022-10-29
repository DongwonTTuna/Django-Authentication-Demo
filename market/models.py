from django.db import models

from datetime import datetime
import uuid
# Create your models here.



class ProductItem(models.Model):
    p_id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=100,blank=False, null=False)
    description = models.TextField(max_length=800, blank=True, null=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.IntegerField(blank=False, null=False)
    
    class Meta:
        verbose_name = 'Item List'
    

    
class Orders(models.Model):
    orderid = models.UUIDField(default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    u_id = models.IntegerField(blank=False, null=False)
    p_id = models.IntegerField(blank=False, null=False)
    status = models.IntegerField(blank=False, null=False)
    
    class Meta:
        verbose_name = 'Order list'