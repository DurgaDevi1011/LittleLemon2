from django.db import models

# Create your models here.

class Booking(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField(6)
    bookingdate = models.DateTimeField()

    class Meta:
        db_table = 'booking'

class Menu(models.Model):
    id = models.AutoField(primary_key=True) 
    tittle = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField(5)

    def __str__(self):
        return f'{self.tittle } : {self.price}'
        
    class Meta:
        db_table = 'menu'