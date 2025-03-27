from django.db import models

class Farmer(models.Model):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)

    def __str__(self):
        return self.name  # This ensures the Farmer's name appears in the admin list


class MulberryFarm(models.Model):
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    location = models.CharField(max_length=200)
    size = models.FloatField()  # Size in acres

class SilkwormBatch(models.Model):
    farm = models.ForeignKey(MulberryFarm, on_delete=models.CASCADE)
    breed_type = models.CharField(max_length=100)
    quantity = models.IntegerField()
    start_date = models.DateField()
    harvest_date = models.DateField()
