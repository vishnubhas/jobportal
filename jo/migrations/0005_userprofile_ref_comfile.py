# Generated by Django 4.2 on 2023-05-04 06:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comapny', '0003_companyprofile_ref_admin'),
        ('jo', '0004_userprofile_ref_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='ref_comfile',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='comapny.jobpost'),
            preserve_default=False,
        ),
    ]