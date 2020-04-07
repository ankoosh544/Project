from django.db import models
class FoodItemsModel(models.Model):
    ino = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=10)
    price = models.FloatField()
    def __str__(self):
        return self.name

class CustomerModel(models.Model):
    cno = models.IntegerField(primary_key=True)
    cname = models.CharField(max_length=10)
    contactno = models.IntegerField()
    foodid = models.ManyToManyField(FoodItemsModel)