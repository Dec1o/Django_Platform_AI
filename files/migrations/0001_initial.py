# Generated by Django 5.1.1 on 2024-10-02 14:34

import django.db.models.deletion
import files.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('companies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PDFFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to=files.models.PDFFile.generate_file_path)),
                ('data_upload', models.DateTimeField(auto_now_add=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pdfs', to='companies.company')),
            ],
        ),
    ]
