# Generated by Django 4.2 on 2023-07-28 06:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_delete_user_user2'),
        ('comapny', '0006_remove_companyprofile_ref_admin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='companyprofile',
            name='work',
        ),
        migrations.RemoveField(
            model_name='companyprofile',
            name='workdisc',
        ),
        migrations.RemoveField(
            model_name='companyprofile',
            name='workpic',
        ),
        migrations.CreateModel(
            name='RecentWork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Post_date', models.DateTimeField(auto_created=True)),
                ('work', models.CharField(max_length=200)),
                ('image', models.ImageField(blank=True, null=True, upload_to='work_image/')),
                ('short_dic', models.CharField(max_length=200)),
                ('long_dic', models.CharField(max_length=200)),
                ('ref_company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.company')),
            ],
        ),
    ]
