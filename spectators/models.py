# models.py

from django.db import models

class Spectators(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    user_type = models.IntegerField(default=4)  
    is_superuser = models.IntegerField(default=1, null=True)
    is_active = models.IntegerField(default=1, null=True)
    wallet = models.FloatField(default=1000) 

    
    class Meta:
        managed = False  
        db_table = 'Users'  
 
