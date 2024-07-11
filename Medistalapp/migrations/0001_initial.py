# Generated by Django 5.0.6 on 2024-07-05 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('prize', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=50)),
                ('quantity', models.IntegerField()),
                ('description', models.TextField()),
            ],
        ),
    ]
