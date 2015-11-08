# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timestamp', models.DateTimeField(verbose_name=b'date submitted')),
                ('survey_date', models.DateField(verbose_name=b'date surveyed')),
                ('user_email', models.EmailField(max_length=254)),
            ],
        ),
    ]
