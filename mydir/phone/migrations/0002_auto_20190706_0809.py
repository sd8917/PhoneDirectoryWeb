# Generated by Django 2.1.2 on 2019-07-06 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phone', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='Phone_Number',
            field=models.BigIntegerField(),
        ),
    ]
