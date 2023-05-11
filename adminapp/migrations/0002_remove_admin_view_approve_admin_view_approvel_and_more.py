# Generated by Django 4.2 on 2023-05-04 07:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_delete_user_user2'),
        ('adminapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='admin_view',
            name='approve',
        ),
        migrations.AddField(
            model_name='admin_view',
            name='approvel',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='admin_view',
            name='ref_comapany_name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='account.company'),
            preserve_default=False,
        ),
    ]
