from django.db import models
# models.py

from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    # Other fields...

    def __str__(self):
        return self.name
