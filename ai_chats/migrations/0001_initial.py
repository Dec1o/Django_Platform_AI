import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('groups_files', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AIChat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat_name', models.CharField(max_length=255)),
                ('temperature', models.FloatField(default=0.7)),
                ('prompt', models.TextField()),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ai_chats', to='groups_files.groupfile')),
            ],
        ),
    ]
