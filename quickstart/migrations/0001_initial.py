# Generated by Django 3.2 on 2021-04-12 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ime', models.CharField(max_length=30)),
                ('prezime', models.CharField(max_length=30)),
                ('br_indeksa', models.CharField(max_length=10)),
            ],
        ),
    ]
