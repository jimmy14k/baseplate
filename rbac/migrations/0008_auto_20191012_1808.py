# Generated by Django 2.1.7 on 2019-10-12 18:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rbac', '0007_auto_20191011_1705'),
    ]

    operations = [
        migrations.RenameField(
            model_name='department',
            old_name='name',
            new_name='dep_name',
        ),
    ]
