from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.
class Expense(models.Model):
    text = models.CharField(max_length=225)
    date = models.DateTimeField()
    amount = models.BigIntegerField()
    user = models.ForeignKey(User , on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user} - {self.text} - {self.amount} - {self.date}'

class Income(models.Model):
    text = models.CharField(max_length=225)
    date = models.DateTimeField()
    amount = models.BigIntegerField()
    user = models.ForeignKey(User , on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user} - {self.text} - {self.amount} - {self.date}'