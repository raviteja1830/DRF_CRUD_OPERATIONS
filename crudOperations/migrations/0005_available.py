# Generated by Django 3.2.5 on 2021-08-10 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudOperations', '0004_games_game_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Available',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=50)),
                ('store', models.CharField(choices=[('STEAMAPP', 'steamapp'), ('ORIGINAPP', 'originapp'), ('EPIC GAME LAUNCHER', 'epic game launcher'), ('BATTLENET', 'battlenet')], max_length=50, null=True)),
            ],
        ),
    ]
