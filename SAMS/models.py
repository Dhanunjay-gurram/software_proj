# myapp/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models

class Users(AbstractUser):
    USER_TYPE_CHOICES = (
        (1, 'Manager'),
        (2, 'Account Clerk'),
        (3, 'Salesperson'),
        (4, 'Spectator'),
    )
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, default=4)

    class Meta:
        db_table = 'Users'
