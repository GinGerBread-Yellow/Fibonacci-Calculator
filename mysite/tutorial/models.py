from django.db import models

# Create your models here.

class OrderItem(models.Model):
    order = models.PositiveIntegerField()