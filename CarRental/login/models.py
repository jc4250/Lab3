from django.db import models

class register(models.Model):
    username= models.CharField(max_length=20,primary_key=True)
    password= models.CharField(max_length=15)
    first_name=models.CharField(max_length=15)
    last_name=models.CharField(max_length=15)
    email_id=models.EmailField()



