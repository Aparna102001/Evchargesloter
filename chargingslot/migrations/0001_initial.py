# Generated by Django 4.1.6 on 2023-04-13 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='slotpoints',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pumpname', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('time', models.IntegerField()),
            ],
        ),
    ]
