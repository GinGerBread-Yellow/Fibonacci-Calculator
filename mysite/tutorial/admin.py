from django.contrib import admin
from rest_framework.permissions import OR
from .models import OrderItem

# Register your models here.

admin.site.register(OrderItem)