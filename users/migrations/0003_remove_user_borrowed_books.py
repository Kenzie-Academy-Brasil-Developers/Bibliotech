# Generated by Django 4.0.6 on 2022-07-21 01:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_borrowed_books'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='borrowed_books',
        ),
    ]
