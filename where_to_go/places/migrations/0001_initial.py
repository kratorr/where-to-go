# Generated by Django 3.1.2 on 2020-10-31 09:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('description_short', models.CharField(max_length=500, verbose_name='Короткое описание')),
                ('description_long', models.TextField(verbose_name='Полное описание')),
                ('longitude', models.FloatField(verbose_name='Долгота')),
                ('latitude', models.FloatField(verbose_name='Широта')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('number', models.PositiveIntegerField()),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='places.place')),
            ],
            options={
                'unique_together': {('place', 'number')},
            },
        ),
    ]
