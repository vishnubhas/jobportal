# Generated by Django 4.2 on 2023-05-02 05:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_delete_user_user2'),
        ('comapny', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='companyprofile',
            name='ref_comodel',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='account.company'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jobpost',
            name='ref_company',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='account.company'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jobpost',
            name='refmodel',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='comapny.companyprofile'),
            preserve_default=False,
        ),
    ]