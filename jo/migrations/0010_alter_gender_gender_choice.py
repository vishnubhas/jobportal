# Generated by Django 4.2 on 2023-08-06 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jo', '0009_remove_gender_gender_remove_marital_marital_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gender',
            name='gender_choice',
            field=models.CharField(max_length=200),
        ),
    ]