# Generated by Django 3.1.4 on 2021-07-05 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thimble', '0007_auto_20210705_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thimble',
            name='description',
            field=models.TextField(),
        ),
    ]