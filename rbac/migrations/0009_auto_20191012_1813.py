# Generated by Django 2.1.7 on 2019-10-12 18:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rbac', '0008_auto_20191012_1808'),
    ]

    operations = [
        migrations.RenameField(
            model_name='department',
            old_name='dep_name',
            new_name='name',
        ),
    ]