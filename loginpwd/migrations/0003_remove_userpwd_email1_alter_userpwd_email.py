# Generated by Django 4.1.4 on 2023-01-07 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginpwd', '0002_userpwd_email1_alter_userpwd_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userpwd',
            name='email1',
        ),
        migrations.AlterField(
            model_name='userpwd',
            name='email',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
