# Generated by Django 3.1.4 on 2021-01-21 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Thimble',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('matherial', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('seria', models.CharField(max_length=200)),
                ('stellaj', models.CharField(max_length=200)),
                ('shelf', models.CharField(max_length=200)),
                ('where', models.CharField(max_length=200)),
                ('who_present', models.CharField(max_length=200)),
                ('date', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('type', models.CharField(choices=[('Обычный', 'Обычный'), ('Рабочий', 'Рабочий'), ('Сувенирный', 'Сувенирный')], max_length=10)),
            ],
        ),
    ]
