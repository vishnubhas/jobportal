# Generated by Django 4.2 on 2023-08-04 16:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comapny', '0016_jobpost_image_jobpost_job_type_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobpost',
            name='ref_company_job',
        ),
    ]
