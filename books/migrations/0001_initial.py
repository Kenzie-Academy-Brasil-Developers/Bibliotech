# Generated by Django 4.0.6 on 2022-07-21 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('genres', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=127)),
                ('pages', models.PositiveIntegerField()),
                ('author', models.CharField(max_length=50)),
                ('classification', models.PositiveIntegerField()),
                ('genre', models.ManyToManyField(related_name='book', to='genres.genre')),
            ],
        ),
    ]
