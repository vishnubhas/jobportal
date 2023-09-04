# Generated by Django 4.2 on 2023-08-08 15:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jo', '0016_userprofile_ref_job'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobapplication',
            name='education',
        ),
        migrations.RemoveField(
            model_name='jobapplication',
            name='email',
        ),
        migrations.RemoveField(
            model_name='jobapplication',
            name='experiance',
        ),
        migrations.RemoveField(
            model_name='jobapplication',
            name='is_confirm',
        ),
        migrations.RemoveField(
            model_name='jobapplication',
            name='name',
        ),
        migrations.RemoveField(
            model_name='jobapplication',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='jobapplication',
            name='skill',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='ref_job',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='jo.jobapplication'),
        ),
    ]