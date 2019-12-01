# Generated by Django 2.2.4 on 2019-09-13 16:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vendor', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_title', models.CharField(max_length=200, verbose_name='project title')),
                ('project_owner', models.TextField(blank=True, max_length=2000, null=True, verbose_name='project owner')),
                ('blueprint_title', models.CharField(max_length=200, verbose_name='blueprint title')),
                ('blueprint', models.TextField(blank=True, max_length=2000, null=True, verbose_name='blueprint')),
                ('changes', models.TextField(blank=True, max_length=2000, null=True, verbose_name='changes')),
                ('release', models.TextField(blank=True, max_length=2000, null=True, verbose_name='release')),
                ('register_date', models.DateField(blank=True, null=True, verbose_name='register date')),
                ('target_implement_date', models.DateField(blank=True, null=True, verbose_name='target implement date')),
                ('actual_implement_date', models.DateField(blank=True, null=True, verbose_name='actual implement date')),
                ('state', models.CharField(choices=[('A', 'Active/In Progress'), ('C', 'Completed'), ('W', 'Waiting/Pending'), ('E', 'Explore/Requirement Not Clear'), ('N', 'Next Year'), ('D', 'Drop/Reject/Cancel')], default='A', max_length=20, verbose_name='state')),
                ('mandays', models.TextField(blank=True, max_length=2000, null=True, verbose_name='mandays')),
                ('remarks', models.TextField(blank=True, max_length=2000, null=True, verbose_name='remarks')),
                ('references', models.TextField(blank=True, max_length=2000, null=True, verbose_name='references')),
                ('priority', models.CharField(choices=[('00_low', 'Low'), ('10_normal', 'Normal'), ('20_high', 'High'), ('30_critical', 'Critical'), ('40_blocker', 'Blocker')], default='10_normal', max_length=20, verbose_name='priority')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('last_modified', models.DateTimeField(auto_now=True, verbose_name='last modified')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='users_created', to=settings.AUTH_USER_MODEL, verbose_name='created by')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='project_buat', to=settings.AUTH_USER_MODEL, verbose_name='PIC IT')),
                ('vendor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='vendor.Vendor')),
            ],
            options={
                'verbose_name': 'Project',
                'verbose_name_plural': 'Projects',
            },
        ),
    ]
