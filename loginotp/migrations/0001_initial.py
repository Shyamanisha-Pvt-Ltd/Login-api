# Generated by Django 4.1.4 on 2023-01-07 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserOTP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Mobile', models.BigIntegerField()),
                ('isVerified', models.BooleanField(default=False)),
                ('counter', models.IntegerField(default=0)),
            ],
        ),
    ]
