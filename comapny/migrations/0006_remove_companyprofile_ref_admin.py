# Generated by Django 4.2 on 2023-07-28 06:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comapny', '0005_remove_companyprofile_ref_comodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='companyprofile',
            name='ref_admin',
        ),
    ]
