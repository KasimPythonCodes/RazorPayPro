# Generated by Django 3.2.6 on 2021-11-07 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coffee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('amount', models.CharField(max_length=70)),
                ('payment_id', models.CharField(max_length=70)),
                ('padi', models.BooleanField(default=False)),
            ],
        ),
    ]
