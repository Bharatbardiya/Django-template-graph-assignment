# Generated by Django 4.2.9 on 2024-01-23 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PrimarySchool',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('district_name', models.CharField(max_length=50)),
                ('medium', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=50)),
            ],
        ),
    ]
