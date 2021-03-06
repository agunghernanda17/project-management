# Generated by Django 2.2.4 on 2019-09-13 16:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vendor', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Aplikasi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='name')),
                ('project_owner', models.CharField(blank=True, max_length=50, null=True, verbose_name='project owner')),
                ('comment', models.TextField(blank=True, max_length=2000, null=True, verbose_name='comment')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('last_modified', models.DateTimeField(auto_now=True, verbose_name='last modified')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='aplikasi_created', to=settings.AUTH_USER_MODEL, verbose_name='created by')),
                ('vendor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='vendor.Vendor')),
            ],
            options={
                'verbose_name': 'Aplikasi',
                'verbose_name_plural': 'Aplikasi',
                'ordering': ['name'],
            },
        ),
    ]
