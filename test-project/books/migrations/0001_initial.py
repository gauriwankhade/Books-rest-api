# Generated by Django 3.1.4 on 2021-01-03 07:22

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('url', models.URLField(max_length=255)),
                ('is_downloaded', models.BooleanField(default=False)),
                ('downloaded_url', models.URLField(default=None, max_length=255)),
            ],
        ),
    ]
