# Generated by Django 3.1.4 on 2021-07-03 15:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('thimble', '0003_auto_20210703_1831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thimble',
            name='country',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='thimble.country'),
        ),
    ]
