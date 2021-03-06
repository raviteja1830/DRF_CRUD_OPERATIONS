# Generated by Django 3.2.5 on 2021-08-10 07:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Games',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('Game_Name', models.TextField(blank=True)),
                ('Game_Type', models.CharField(choices=[('Battle Royale', 'battle royale'), ('Areans', 'areans'), ('RPG', 'rpg'), ('SC_FI', 'sc_fi'), ('Horror', 'horror')], default='Battle royale', max_length=50)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
