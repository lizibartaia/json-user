from django.db import models

# Create your models here.

from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    # Add any other relevant fields

    def __str__(self):
        return self.name