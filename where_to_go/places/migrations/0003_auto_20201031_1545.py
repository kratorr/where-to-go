# Generated by Django 3.1.2 on 2020-10-31 15:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0002_auto_20201031_1538'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['number']},
        ),
        migrations.AlterUniqueTogether(
            name='image',
            unique_together=set(),
        ),
    ]
