# Generated by Django 4.0.6 on 2022-07-28 05:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_rename_tdata_tmodels'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tmodels',
            name='file',
        ),
    ]
