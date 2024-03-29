# Generated by Django 4.2.4 on 2023-08-26 11:34

import datetime
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
            name='Box',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('length', models.IntegerField(default=0, help_text='Length of Box')),
                ('width', models.IntegerField(default=0, help_text='Width of Box')),
                ('height', models.IntegerField(default=0, help_text='Height of Box')),
                ('area', models.IntegerField(default=0, help_text='Area of Box')),
                ('volume', models.IntegerField(default=0, help_text='Volume of Box')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(default=datetime.datetime.now)),
                ('created_by', models.ForeignKey(help_text='User Created', on_delete=django.db.models.deletion.CASCADE, related_name='created_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
