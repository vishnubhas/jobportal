# Generated by Django 4.2 on 2023-08-09 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comapny', '0021_remove_jobpost_ref_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyprofile',
            name='gits',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='companyprofile',
            name='websites',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='companyprofile',
            name='youtubes',
            field=models.CharField(max_length=300),
        ),
    ]
