# Generated by Django 3.1.4 on 2021-07-07 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thimble', '0008_auto_20210705_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thimble',
            name='type',
            field=models.CharField(choices=[('Обычный', 'Обычный'), ('Церковный', 'Церковный'), ('Рабочий', 'Рабочий'), ('Народные промыслы', 'Народные промыслы'), ('Совы', 'Совы'), ('Известные личности', 'Известные личности')], max_length=200),
        ),
    ]