# Generated by Django 3.2.5 on 2021-08-10 11:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crudOperations', '0009_auto_20210810_1716'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Available',
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]
