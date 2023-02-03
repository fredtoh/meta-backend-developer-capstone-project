from django.db import models

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField()
    bookingDate = models.DateTimeField(db_index=True)


class Menu(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()
    #add the following method in Menu class
    def get_item(self):
        return f'{self.title} : {str(self.price)}'

    def __str__(self)-> str:
        return self.title