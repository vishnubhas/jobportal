# Generated by Django 4.2 on 2023-08-30 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jo', '0027_language'),
    ]

    operations = [
        migrations.AddField(
            model_name='language',
            name='level',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]