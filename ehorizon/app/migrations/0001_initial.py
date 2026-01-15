
import app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PitchRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=120)),
                ('trl_level', models.IntegerField()),
                ('theme', models.CharField(max_length=50)),
                ('abstract_pdf', models.FileField(upload_to=app.models.abstract_upload_path)),
                ('members', models.JSONField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
