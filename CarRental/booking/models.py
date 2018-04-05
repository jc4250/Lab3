from django.db import models

class cars(models.Model):
    company=models.CharField(max_length=15)
    model_name=models.CharField(max_length=15)
    car_id=models.CharField(max_length=15,primary_key=True)
    seat=models.CharField(max_length=3)
    hour_price=models.CharField(max_length=5)
    type=models.CharField(max_length=15)
    position=models.CharField(max_length=30)
    images=models.CharField(max_length=25)
    availability=models.CharField(max_length=10,default=" ")


class Booking(models.Model):
    username = models.CharField(max_length=20)
    car_id=models.CharField(max_length=15)
    pickup_location=models.CharField(max_length=30)
    dropoff_location=models.CharField(max_length=30)
    pickup_date=models.CharField(max_length=15)
    pickup_time = models.CharField(max_length=15)
    dropoff_date = models.CharField(max_length=15)
    dropoff_time = models.CharField(max_length=15)
    driver=models.CharField(max_length=15)



