# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import re
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(max_length=255, validators=[django.core.validators.RegexValidator(re.compile(b'^[\\w.@+-]+$'), 'Enter a valid username.', 'invalid')], help_text='Required. 255 characters or fewer. Letters, numbers and @/./+/-/_ characters', unique=True, verbose_name=b'Username', db_index=True)),
                ('email', models.EmailField(db_index=True, unique=True, max_length=255, verbose_name=b'Email', blank=True)),
                ('first_name', models.CharField(max_length=20, verbose_name=b'First_Name')),
                ('last_name', models.CharField(max_length=20, verbose_name=b'Last_Name')),
                ('timezone', models.CharField(max_length=250, null=True, verbose_name=b'Timezone Information', blank=True)),
                ('is_active', models.BooleanField(default=False, verbose_name=b'Active User')),
                ('is_staff', models.BooleanField(default=False, verbose_name=b'Staff User')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name=b'Created_At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name=b'Updated_At')),
                ('groups', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Group', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Permission', blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
