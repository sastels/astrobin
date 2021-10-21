# Generated by Django 2.2.24 on 2021-09-06 19:20

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('astrobin_apps_equipment', '0012_add_other_camera_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='camera',
            name='reviewed_by',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL,
                                    related_name='astrobin_apps_equipment_cameras_reviewed',
                                    to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='camera',
            name='reviewed_timestamp',
            field=models.DateTimeField(editable=False, null=True),
        ),
        migrations.AddField(
            model_name='camera',
            name='reviewer_comment',
            field=models.TextField(editable=False, null=True),
        ),
        migrations.AddField(
            model_name='camera',
            name='reviewer_decision',
            field=models.CharField(choices=[('ACCEPTED', 'Accepted'), ('REJECTED', 'Rejected')], editable=False,
                                   max_length=8, null=True),
        ),
        migrations.AddField(
            model_name='sensor',
            name='reviewed_by',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL,
                                    related_name='astrobin_apps_equipment_sensors_reviewed',
                                    to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='sensor',
            name='reviewed_timestamp',
            field=models.DateTimeField(editable=False, null=True),
        ),
        migrations.AddField(
            model_name='sensor',
            name='reviewer_comment',
            field=models.TextField(editable=False, null=True),
        ),
        migrations.AddField(
            model_name='sensor',
            name='reviewer_decision',
            field=models.CharField(choices=[('ACCEPTED', 'Accepted'), ('REJECTED', 'Rejected')], editable=False,
                                   max_length=8, null=True),
        ),
        migrations.AddField(
            model_name='telescope',
            name='reviewed_by',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL,
                                    related_name='astrobin_apps_equipment_telescopes_reviewed',
                                    to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='telescope',
            name='reviewed_timestamp',
            field=models.DateTimeField(editable=False, null=True),
        ),
        migrations.AddField(
            model_name='telescope',
            name='reviewer_comment',
            field=models.TextField(editable=False, null=True),
        ),
        migrations.AddField(
            model_name='telescope',
            name='reviewer_decision',
            field=models.CharField(choices=[('ACCEPTED', 'Accepted'), ('REJECTED', 'Rejected')], editable=False,
                                   max_length=8, null=True),
        ),
    ]
