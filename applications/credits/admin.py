from django.contrib import admin
from .models import Client, CreditRequest
# Register your models here.

admin.site.register(Client)
admin.site.register(CreditRequest)