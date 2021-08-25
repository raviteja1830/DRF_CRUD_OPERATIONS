# Generated by Django 3.2.5 on 2021-08-10 11:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crudOperations', '0007_rename_store_available_purchase_from'),
    ]

    operations = [
        migrations.AddField(
            model_name='available',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='crudOperations.customer'),
        ),
        migrations.AddField(
            model_name='available',
            name='game',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='crudOperations.games'),
        ),
    ]
