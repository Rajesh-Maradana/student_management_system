# Generated by Django 4.1.7 on 2023-04-19 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='last_name',
            field=models.CharField(max_length=90),
        ),
    ]