from django.db import models

# Create your models here.
class Feedback(models.Model):
    email = models.EmailField(max_length=30)
    feedback = models.CharField(max_length=500)
