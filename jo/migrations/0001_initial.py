# Generated by Django 4.2 on 2023-04-22 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Userprofile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('s_name', models.CharField(max_length=250)),
                ('description', models.TextField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('skill', models.CharField(max_length=200)),
                ('git', models.CharField(max_length=300, unique=True)),
                ('youtube', models.CharField(max_length=300, unique=True)),
                ('linkedin', models.CharField(max_length=300, unique=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='image/')),
                ('age', models.IntegerField(verbose_name=3)),
                ('street', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('pincode', models.PositiveBigIntegerField()),
            ],
        ),
    ]
