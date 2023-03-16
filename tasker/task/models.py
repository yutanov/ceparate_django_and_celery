from django.db import models


class NumbersSum(models.Model):
    number_one = models.IntegerField(blank=False)
    number_two = models.IntegerField(blank=False)
    number_sum = models.IntegerField(blank=True, null=True)
