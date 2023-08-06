# Generated by Django 4.2.3 on 2023-08-05 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(error_messages={'blank': 'This field must not be empty', 'max_length': 'This field must not be more than 50 characters', 'null': 'This field must not be empty'}, max_length=50)),
                ('location', models.CharField(max_length=254)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Restaurant',
                'ordering': ('-created_at',),
            },
        ),
    ]
