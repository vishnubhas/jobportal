# Generated by Django 4.2 on 2023-08-17 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comapny', '0022_alter_companyprofile_gits_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='companyprofile',
            name='is_request',
            field=models.BooleanField(default=False),
        ),
    ]
