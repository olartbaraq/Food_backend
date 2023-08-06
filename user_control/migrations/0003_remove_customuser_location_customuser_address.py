# Generated by Django 4.2.3 on 2023-08-01 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_control', '0002_alter_customuser_last_login'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='location',
        ),
        migrations.AddField(
            model_name='customuser',
            name='address',
            field=models.CharField(default='Ibadan', error_messages={'blank': 'This field must not be empty', 'max_length': 'This field must not be more than 100 characters', 'null': 'This field must not be empty'}, max_length=255),
        ),
    ]
