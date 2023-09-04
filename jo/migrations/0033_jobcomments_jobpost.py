# Generated by Django 4.2 on 2023-09-01 12:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comapny', '0023_companyprofile_is_request'),
        ('jo', '0032_jobcomments'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobcomments',
            name='jobpost',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='comapny.jobpost'),
            preserve_default=False,
        ),
    ]
