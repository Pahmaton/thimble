from django.db import models


class Country(models.Model):
    REGION_CHOICES = (
        ('Север Европы', 'Север Европы'),
        ('бывшие сов. республики', 'бывшие сов.республики'),
        ('Ближний Восток', 'Ближний Восток'),
        ('Африка', 'Африка'),
        ('Северная Америка', 'Северная Америка'),
        ('Южная Америка', 'Южная Америка'),
    )
    name = models.CharField(unique=True, max_length=200)
    region = models.CharField(choices=REGION_CHOICES, max_length=200)

    def __str__(self):
        return self.name

class City(models.Model):
    REGION_CHOICES = (
        ('Центральный фед.округ', 'Центральный фед.округ'),
        ('Северо-западный', 'Северо-западный'),
        ('Северный кавказ', 'Северный кавказ'),
        ('Южный', 'Южный'),
        ('Крым', 'Крым'),
        ('Приволжский', 'Приволжский'),
        ('Уральский', 'Уральский'),
        ('Сибирский', 'Сибирский'),
        ('Центральный фед.округ', 'Центральный фед.округ'),
        ('Иностранный', 'Иностранный')
    )
    name = models.CharField(unique=True, max_length=200)
    region = models.CharField(choices=REGION_CHOICES, max_length=200)
    country = models.ForeignKey(Country, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.name


class Thimble(models.Model):
    number = models.CharField(max_length=200)
    country = models.ForeignKey(Country, on_delete=models.PROTECT, null=True)
    city = models.ForeignKey(City, on_delete=models.PROTECT, null=True)
    matherial = models.CharField(max_length=200)
    #created_at = models.DateTimeField(auto_now_add=True)
    THIMBLES_TYPES = (
        ('Обычный', 'Обычный'),
        ('Церковный', 'Церковный'),
        ('Рабочий', 'Рабочий'),
        ('Народные промыслы', 'Народные промыслы'),
        ('Совы', 'Совы'),
        ('Известные личности', 'Известные личности')
    )
    type = models.CharField(max_length=200, choices=THIMBLES_TYPES)
    description = models.TextField()
    image = models.ImageField(upload_to="images")

