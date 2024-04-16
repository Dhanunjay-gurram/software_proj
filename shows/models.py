from django.db import models


class Shows(models.Model):
    # Define your fields here
    show_id = models.AutoField(primary_key=True)
    show_name = models.CharField(max_length=100)
    date = models.DateField()
    timing = models.TimeField()
    end_time = models.TimeField()
    no_of_balcony_seats = models.IntegerField()
    no_of_ordinary_seats = models.IntegerField()
    balcony_rate = models.DecimalField(max_digits=6, decimal_places=2)
    ordinary_rate = models.DecimalField(max_digits=6, decimal_places=2)
    
    class Meta:
        managed = False  
        db_table = 'Shows' 

class Seats(models.Model):
    seat_no = models.CharField(max_length=100)
    empty = models.BooleanField(default=True)
    show_id = models.CharField(max_length=50)
    ID = models.AutoField(primary_key=True)

    class Meta:
        managed = False 
        db_table = 'Seats' 

    def __str__(self):
        return self.show_id

