# Generated by Django 4.0.6 on 2022-07-20 19:29

from django.db import migrations, models
import loans.models


class Migration(migrations.Migration):

    dependencies = [
        ('loans', '0002_alter_loan_return_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='return_date',
            field=models.DateField(default=loans.models.return_date),
        ),
    ]
