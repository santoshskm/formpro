# Generated by Django 2.1.7 on 2019-03-12 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('company', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('designation', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
            ],
        ),
    ]