from django.db import models

# Create your models here.
class InvestmentModel(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100)
    date = models.IntegerField()
    price = models.CharField(max_length=100)
    sum = models.CharField(max_length=100)
    user_id = models.CharField(max_length=100)

    def __str__(self):
        return self.name, self.date, self.price, self.sum, self.user_id