# Generated by Django 5.0.6 on 2024-07-15 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Medistalapp', '0005_appointment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('username', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]
