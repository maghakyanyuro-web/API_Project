from django.db import models

# Create your models here.

class Car(models.Model):

    model = models.CharField(max_length=100)
    price = models.PositiveBigIntegerField()
    year = models.DateField()

    def __str__(self):
        return self.model