# Generated by Django 2.0.2 on 2018-12-01 08:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_auto_20181201_1557'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='image',
            new_name='imagefun',
        ),
    ]
