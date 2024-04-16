from django.db import models
from django.core.validators import MinValueValidator

class Users(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    sales_id = models.IntegerField()
    user_type = models.IntegerField(default=3)  
    is_superuser = models.IntegerField(default=1, null=True)
    is_active = models.IntegerField(default=1, null=True)
    wallet = models.FloatField(default=1000) 

    class Meta:
        managed = False  
        db_table = 'Users'


class BalanceSheet(models.Model):
    show_id = models.IntegerField() 
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    type = models.CharField(max_length = 50) 
    sales_id = models.IntegerField()  
    txn_id = models.AutoField(primary_key=True) 
    
    class Meta:
        db_table = 'BalanceSheet'