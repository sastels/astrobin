# Generated by Django 2.2.24 on 2021-09-06 16:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('astrobin_apps_equipment', '0011_drop_brand_uniqueness_constraint'),
    ]

    operations = [
        migrations.AlterField(
            model_name='camera',
            name='type',
            field=models.CharField(choices=[('DEDICATED_DEEP_SKY', 'Dedicated deep-sky camera'),
                                            ('DSLR_MIRRORLESS', 'General purpose DSLR or mirrorless camera'),
                                            ('GUIDER_PLANETARY', 'Guider/Planetary camera'),
                                            ('VIDEO', 'General purpose video camera'), ('FILM', 'Film camera'),
                                            ('OTHER', 'Other')], max_length=64, verbose_name='Type'),
        ),
    ]
