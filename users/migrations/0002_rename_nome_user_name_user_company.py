# Generated by Django 5.1.1 on 2024-09-18 12:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='nome',
            new_name='name',
        ),
        migrations.AddField(
            model_name='user',
            name='company',
            field=models.ForeignKey(default=6, on_delete=django.db.models.deletion.CASCADE, to='companies.company'),
            preserve_default=False,
        ),
    ]
