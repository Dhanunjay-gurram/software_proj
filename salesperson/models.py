from django.db import models

class Tickets_Info(models.Model):
    seat_no = models.CharField(max_length=100)
    show_name = models.CharField(max_length=100)
    date = models.DateField()
    timing = models.CharField(max_length=50)
    seat_type = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    username = models.CharField(max_length=100)
    show_id = models.CharField(max_length=50)
    sales_id = models.IntegerField()
    booking_id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'Tickets_Info'

    