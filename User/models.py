from django.db import models
from django.contrib.auth.models import User

# Profile Model

class Profile(models.Model):
    staff = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    address = models.CharField(max_length=200, null=True)
    phone_number = models.CharField(max_length=20, null=True)

    def __str__(self):
        return f'{self.staff}-Profile'

