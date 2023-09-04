# Generated by Django 4.2 on 2023-08-08 15:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jo', '0017_remove_jobapplication_education_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='ref_job',
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='ref_profile',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='jo.userprofile'),
            preserve_default=False,
        ),
    ]