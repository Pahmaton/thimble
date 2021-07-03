from django.db import models


class Country(models.Model):
    REGION_CHOICES = (
        ('Обычный', 'Обычный'),
    )
    name = models.CharField(unique=True, max_length=200)
    region = models.CharField(choices=REGION_CHOICES, max_length=200)


class Thimble(models.Model):
    number = models.CharField(max_length=200)
    country = models.ForeignKey(Country, on_delete=models.PROTECT, null=True)
    city = models.CharField(max_length=200)
    matherial = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    seria = models.CharField(max_length=200)
    stellaj = models.CharField(max_length=200)
    shelf = models.CharField(max_length=200)
    where = models.CharField(max_length=200)
    who_present = models.CharField(max_length=200)
    date = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    THIMBLES_TYPES = (
        ('Обычный', 'Обычный'),
        ('Рабочий', 'Рабочий'),
        ('Сувенирный', 'Сувенирный'),
    )
    type = models.CharField(max_length=10, choices=THIMBLES_TYPES)
    image = models.ImageField(upload_to="images")

