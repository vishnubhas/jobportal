# Generated by Django 4.2 on 2023-04-22 11:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jo', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofile',
            options={'ordering': ('name',), 'verbose_name': 'userprofile', 'verbose_name_plural': 'userprofiles'},
        ),
    ]