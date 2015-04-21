# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Santo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('santo', models.CharField(max_length=50)),
                ('fecha', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
