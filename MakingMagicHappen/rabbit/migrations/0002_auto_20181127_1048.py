# Generated by Django 2.0.6 on 2018-11-27 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rabbit', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rabbitprofile',
            name='image',
            field=models.CharField(max_length=400),
        ),
    ]
