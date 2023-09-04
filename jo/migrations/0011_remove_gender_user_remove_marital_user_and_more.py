# Generated by Django 4.2 on 2023-08-06 14:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jo', '0010_alter_gender_gender_choice'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gender',
            name='user',
        ),
        migrations.RemoveField(
            model_name='marital',
            name='user',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='ref_gender',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='jo.gender'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='ref_martial',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='jo.marital'),
            preserve_default=False,
        ),
    ]