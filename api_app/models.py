from django.db import models

# Create your models here.

class Supplies(models.Model):
    Name = models.CharField(max_length=50, null=True)
    Phone_number = models.IntegerField(max_length=12)
    State = models.CharField(max_length=20)
    City = models.CharField(max_length=20)
    Supply_address = models.TextField(max_length=200)
    Description = models.TextField(max_length=1000, default='', help_text='500 words max')
    Approx_quantity_available = models.IntegerField(max_length=10)
    def __str__(self):
        return str(self.State) + " | " + str(self.City)
    class Meta:
        verbose_name_plural = "Supplies"

    