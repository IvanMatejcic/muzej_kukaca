# Generated by Django 3.2.8 on 2021-12-07 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_kukac_kukac_spol'),
    ]

    operations = [
        migrations.AddField(
            model_name='kukac',
            name='kukac_dostupan',
            field=models.BooleanField(default=False),
        ),
    ]
