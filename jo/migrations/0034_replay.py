# Generated by Django 4.2 on 2023-09-02 07:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comapny', '0027_delete_replay'),
        ('jo', '0033_jobcomments_jobpost'),
    ]

    operations = [
        migrations.CreateModel(
            name='Replay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('replay', models.CharField(max_length=200)),
                ('date', models.DateField(auto_now_add=True)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comapny.jobpost')),
                ('jobcomments', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jo.jobcomments')),
                ('ref_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comapny.companyprofile')),
            ],
        ),
    ]
