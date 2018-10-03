# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms_app', '0002_disciplina_disciplinaofertada'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('nome', models.TextField(max_length=255)),
                ('email', models.TextField(max_length=255)),
                ('celular', models.TextField(max_length=20)),
                ('login', models.TextField(max_length=20)),
                ('senha', models.TextField(max_length=20)),
            ],
        ),
    ]
