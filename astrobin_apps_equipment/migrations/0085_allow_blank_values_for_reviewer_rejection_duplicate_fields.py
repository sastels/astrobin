# Generated by Django 2.2.24 on 2022-07-01 13:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('astrobin_apps_equipment', '0084_rename_reviewer_timestamp_to_reviewer_lock_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accessory',
            name='reviewer_rejection_duplicate_of_klass',
            field=models.CharField(
                blank=True,
                choices=[('SENSOR', 'Sensor'), ('CAMERA', 'Camera'), ('TELESCOPE', 'Telescope'), ('MOUNT', 'Mount'),
                         ('FILTER', 'Filter'), ('ACCESSORY', 'Accessory'), ('SOFTWARE', 'Software')], max_length=16,
                null=True
            ),
        ),
        migrations.AlterField(
            model_name='accessory',
            name='reviewer_rejection_duplicate_of_usage_type',
            field=models.CharField(
                blank=True, choices=[('IMAGING', 'Imaging'), ('GUIDING', 'Guiding')], max_length=16, null=True
            ),
        ),
        migrations.AlterField(
            model_name='accessoryeditproposal',
            name='reviewer_rejection_duplicate_of_klass',
            field=models.CharField(
                blank=True,
                choices=[('SENSOR', 'Sensor'), ('CAMERA', 'Camera'), ('TELESCOPE', 'Telescope'), ('MOUNT', 'Mount'),
                         ('FILTER', 'Filter'), ('ACCESSORY', 'Accessory'), ('SOFTWARE', 'Software')], max_length=16,
                null=True
            ),
        ),
        migrations.AlterField(
            model_name='accessoryeditproposal',
            name='reviewer_rejection_duplicate_of_usage_type',
            field=models.CharField(
                blank=True, choices=[('IMAGING', 'Imaging'), ('GUIDING', 'Guiding')], max_length=16, null=True
            ),
        ),
        migrations.AlterField(
            model_name='camera',
            name='reviewer_rejection_duplicate_of_klass',
            field=models.CharField(
                blank=True,
                choices=[('SENSOR', 'Sensor'), ('CAMERA', 'Camera'), ('TELESCOPE', 'Telescope'), ('MOUNT', 'Mount'),
                         ('FILTER', 'Filter'), ('ACCESSORY', 'Accessory'), ('SOFTWARE', 'Software')], max_length=16,
                null=True
            ),
        ),
        migrations.AlterField(
            model_name='camera',
            name='reviewer_rejection_duplicate_of_usage_type',
            field=models.CharField(
                blank=True, choices=[('IMAGING', 'Imaging'), ('GUIDING', 'Guiding')], max_length=16, null=True
            ),
        ),
        migrations.AlterField(
            model_name='cameraeditproposal',
            name='reviewer_rejection_duplicate_of_klass',
            field=models.CharField(
                blank=True,
                choices=[('SENSOR', 'Sensor'), ('CAMERA', 'Camera'), ('TELESCOPE', 'Telescope'), ('MOUNT', 'Mount'),
                         ('FILTER', 'Filter'), ('ACCESSORY', 'Accessory'), ('SOFTWARE', 'Software')], max_length=16,
                null=True
            ),
        ),
        migrations.AlterField(
            model_name='cameraeditproposal',
            name='reviewer_rejection_duplicate_of_usage_type',
            field=models.CharField(
                blank=True, choices=[('IMAGING', 'Imaging'), ('GUIDING', 'Guiding')], max_length=16, null=True
            ),
        ),
        migrations.AlterField(
            model_name='filter',
            name='reviewer_rejection_duplicate_of_klass',
            field=models.CharField(
                blank=True,
                choices=[('SENSOR', 'Sensor'), ('CAMERA', 'Camera'), ('TELESCOPE', 'Telescope'), ('MOUNT', 'Mount'),
                         ('FILTER', 'Filter'), ('ACCESSORY', 'Accessory'), ('SOFTWARE', 'Software')], max_length=16,
                null=True
            ),
        ),
        migrations.AlterField(
            model_name='filter',
            name='reviewer_rejection_duplicate_of_usage_type',
            field=models.CharField(
                blank=True, choices=[('IMAGING', 'Imaging'), ('GUIDING', 'Guiding')], max_length=16, null=True
            ),
        ),
        migrations.AlterField(
            model_name='filtereditproposal',
            name='reviewer_rejection_duplicate_of_klass',
            field=models.CharField(
                blank=True,
                choices=[('SENSOR', 'Sensor'), ('CAMERA', 'Camera'), ('TELESCOPE', 'Telescope'), ('MOUNT', 'Mount'),
                         ('FILTER', 'Filter'), ('ACCESSORY', 'Accessory'), ('SOFTWARE', 'Software')], max_length=16,
                null=True
            ),
        ),
        migrations.AlterField(
            model_name='filtereditproposal',
            name='reviewer_rejection_duplicate_of_usage_type',
            field=models.CharField(
                blank=True, choices=[('IMAGING', 'Imaging'), ('GUIDING', 'Guiding')], max_length=16, null=True
            ),
        ),
        migrations.AlterField(
            model_name='mount',
            name='reviewer_rejection_duplicate_of_klass',
            field=models.CharField(
                blank=True,
                choices=[('SENSOR', 'Sensor'), ('CAMERA', 'Camera'), ('TELESCOPE', 'Telescope'), ('MOUNT', 'Mount'),
                         ('FILTER', 'Filter'), ('ACCESSORY', 'Accessory'), ('SOFTWARE', 'Software')], max_length=16,
                null=True
            ),
        ),
        migrations.AlterField(
            model_name='mount',
            name='reviewer_rejection_duplicate_of_usage_type',
            field=models.CharField(
                blank=True, choices=[('IMAGING', 'Imaging'), ('GUIDING', 'Guiding')], max_length=16, null=True
            ),
        ),
        migrations.AlterField(
            model_name='mounteditproposal',
            name='reviewer_rejection_duplicate_of_klass',
            field=models.CharField(
                blank=True,
                choices=[('SENSOR', 'Sensor'), ('CAMERA', 'Camera'), ('TELESCOPE', 'Telescope'), ('MOUNT', 'Mount'),
                         ('FILTER', 'Filter'), ('ACCESSORY', 'Accessory'), ('SOFTWARE', 'Software')], max_length=16,
                null=True
            ),
        ),
        migrations.AlterField(
            model_name='mounteditproposal',
            name='reviewer_rejection_duplicate_of_usage_type',
            field=models.CharField(
                blank=True, choices=[('IMAGING', 'Imaging'), ('GUIDING', 'Guiding')], max_length=16, null=True
            ),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='reviewer_rejection_duplicate_of_klass',
            field=models.CharField(
                blank=True,
                choices=[('SENSOR', 'Sensor'), ('CAMERA', 'Camera'), ('TELESCOPE', 'Telescope'), ('MOUNT', 'Mount'),
                         ('FILTER', 'Filter'), ('ACCESSORY', 'Accessory'), ('SOFTWARE', 'Software')], max_length=16,
                null=True
            ),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='reviewer_rejection_duplicate_of_usage_type',
            field=models.CharField(
                blank=True, choices=[('IMAGING', 'Imaging'), ('GUIDING', 'Guiding')], max_length=16, null=True
            ),
        ),
        migrations.AlterField(
            model_name='sensoreditproposal',
            name='reviewer_rejection_duplicate_of_klass',
            field=models.CharField(
                blank=True,
                choices=[('SENSOR', 'Sensor'), ('CAMERA', 'Camera'), ('TELESCOPE', 'Telescope'), ('MOUNT', 'Mount'),
                         ('FILTER', 'Filter'), ('ACCESSORY', 'Accessory'), ('SOFTWARE', 'Software')], max_length=16,
                null=True
            ),
        ),
        migrations.AlterField(
            model_name='sensoreditproposal',
            name='reviewer_rejection_duplicate_of_usage_type',
            field=models.CharField(
                blank=True, choices=[('IMAGING', 'Imaging'), ('GUIDING', 'Guiding')], max_length=16, null=True
            ),
        ),
        migrations.AlterField(
            model_name='software',
            name='reviewer_rejection_duplicate_of_klass',
            field=models.CharField(
                blank=True,
                choices=[('SENSOR', 'Sensor'), ('CAMERA', 'Camera'), ('TELESCOPE', 'Telescope'), ('MOUNT', 'Mount'),
                         ('FILTER', 'Filter'), ('ACCESSORY', 'Accessory'), ('SOFTWARE', 'Software')], max_length=16,
                null=True
            ),
        ),
        migrations.AlterField(
            model_name='software',
            name='reviewer_rejection_duplicate_of_usage_type',
            field=models.CharField(
                blank=True, choices=[('IMAGING', 'Imaging'), ('GUIDING', 'Guiding')], max_length=16, null=True
            ),
        ),
        migrations.AlterField(
            model_name='softwareeditproposal',
            name='reviewer_rejection_duplicate_of_klass',
            field=models.CharField(
                blank=True,
                choices=[('SENSOR', 'Sensor'), ('CAMERA', 'Camera'), ('TELESCOPE', 'Telescope'), ('MOUNT', 'Mount'),
                         ('FILTER', 'Filter'), ('ACCESSORY', 'Accessory'), ('SOFTWARE', 'Software')], max_length=16,
                null=True
            ),
        ),
        migrations.AlterField(
            model_name='softwareeditproposal',
            name='reviewer_rejection_duplicate_of_usage_type',
            field=models.CharField(
                blank=True, choices=[('IMAGING', 'Imaging'), ('GUIDING', 'Guiding')], max_length=16, null=True
            ),
        ),
        migrations.AlterField(
            model_name='telescope',
            name='reviewer_rejection_duplicate_of_klass',
            field=models.CharField(
                blank=True,
                choices=[('SENSOR', 'Sensor'), ('CAMERA', 'Camera'), ('TELESCOPE', 'Telescope'), ('MOUNT', 'Mount'),
                         ('FILTER', 'Filter'), ('ACCESSORY', 'Accessory'), ('SOFTWARE', 'Software')], max_length=16,
                null=True
            ),
        ),
        migrations.AlterField(
            model_name='telescope',
            name='reviewer_rejection_duplicate_of_usage_type',
            field=models.CharField(
                blank=True, choices=[('IMAGING', 'Imaging'), ('GUIDING', 'Guiding')], max_length=16, null=True
            ),
        ),
        migrations.AlterField(
            model_name='telescopeeditproposal',
            name='reviewer_rejection_duplicate_of_klass',
            field=models.CharField(
                blank=True,
                choices=[('SENSOR', 'Sensor'), ('CAMERA', 'Camera'), ('TELESCOPE', 'Telescope'), ('MOUNT', 'Mount'),
                         ('FILTER', 'Filter'), ('ACCESSORY', 'Accessory'), ('SOFTWARE', 'Software')], max_length=16,
                null=True
            ),
        ),
        migrations.AlterField(
            model_name='telescopeeditproposal',
            name='reviewer_rejection_duplicate_of_usage_type',
            field=models.CharField(
                blank=True, choices=[('IMAGING', 'Imaging'), ('GUIDING', 'Guiding')], max_length=16, null=True
            ),
        ),
    ]
