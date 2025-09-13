from django.db import models
from django.contrib import admin

class Car_DB(models.Model):
    car_brand=models.CharField(max_length=10)
    order_id=models.IntegerField(primary_key=True)
    car_model=models.CharField()
    price=models.IntegerField()
    purchase_date=models.DateField()

class Car_DBAdmin(admin.ModelAdmin):
    list_display=["car_brand","order_id","car_model","price","purchase_date"]