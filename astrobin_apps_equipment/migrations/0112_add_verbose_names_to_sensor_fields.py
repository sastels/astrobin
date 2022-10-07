# Generated by Django 2.2.24 on 2022-10-07 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('astrobin_apps_equipment', '0111_add_verbose_name_to_camera_sensor_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensor',
            name='adc',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='ADC'),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='color_or_mono',
            field=models.CharField(blank=True, choices=[('C', 'Color'), ('M', 'Monochromatic')], max_length=1, null=True, verbose_name='Color or mono'),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='full_well_capacity',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='Full well capacity'),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='pixel_height',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Pixel height'),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='pixel_size',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='Pixel size (μm)'),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='pixel_width',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Pixel width'),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='quantum_efficiency',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Quantum efficiency'),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='read_noise',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='Read noise (e-)'),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='sensor_height',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='Sensor height (mm)'),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='sensor_width',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='Sensor width (mm)'),
        ),
        migrations.AlterField(
            model_name='sensoreditproposal',
            name='adc',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='ADC'),
        ),
        migrations.AlterField(
            model_name='sensoreditproposal',
            name='color_or_mono',
            field=models.CharField(blank=True, choices=[('C', 'Color'), ('M', 'Monochromatic')], max_length=1, null=True, verbose_name='Color or mono'),
        ),
        migrations.AlterField(
            model_name='sensoreditproposal',
            name='full_well_capacity',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='Full well capacity'),
        ),
        migrations.AlterField(
            model_name='sensoreditproposal',
            name='pixel_height',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Pixel height'),
        ),
        migrations.AlterField(
            model_name='sensoreditproposal',
            name='pixel_size',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='Pixel size (μm)'),
        ),
        migrations.AlterField(
            model_name='sensoreditproposal',
            name='pixel_width',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Pixel width'),
        ),
        migrations.AlterField(
            model_name='sensoreditproposal',
            name='quantum_efficiency',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Quantum efficiency'),
        ),
        migrations.AlterField(
            model_name='sensoreditproposal',
            name='read_noise',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='Read noise (e-)'),
        ),
        migrations.AlterField(
            model_name='sensoreditproposal',
            name='sensor_height',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='Sensor height (mm)'),
        ),
        migrations.AlterField(
            model_name='sensoreditproposal',
            name='sensor_width',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='Sensor width (mm)'),
        ),
    ]
