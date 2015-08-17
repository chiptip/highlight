# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('source_url', models.CharField(max_length=255)),
                ('duration', models.IntegerField()),
                ('thumbnail_url', models.CharField(max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('video', models.FileField(upload_to='original')),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
    ]
