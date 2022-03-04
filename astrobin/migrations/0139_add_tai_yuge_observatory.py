# Generated by Django 2.2.24 on 2022-03-04 09:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('astrobin', '0138_add_exposure_per_frame'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='remote_source',
            field=models.CharField(
                blank=True,
                choices=[(None, '---------'), ('OWN', 'Non-commercial independent facility'), (None, '---------'),
                         ('AC', 'AstroCamp'), ('AHK', 'Astro Hostel Krasnodar'),
                         ('AOWA', 'Astro Observatories Western Australia'), ('CS', 'ChileScope'),
                         ('DSNM', 'Dark Sky New Mexico'), ('DSP', 'Dark Sky Portal'), ('DSV', 'Deepsky Villa'),
                         ('DSC', 'DeepSkyChile'), ('DSW', 'DeepSkyWest'), ('eEyE', 'e-EyE Extremadura'),
                         ('EITS', 'Eye In The Sky'), ('GFA', 'Goldfield Astronomical Observatory'),
                         ('GMO', 'Grand Mesa Observatory'), ('HMO', "Heaven's Mirror Observatory"),
                         ('IC', 'IC Astronomy Observatories'), ('ITU', 'Image The Universe'),
                         ('INS', 'Insight Observatory'), ('ITELESCO', 'iTelescope'),
                         ('LGO', 'Lijiang Gemini Observatory'),
                         ('MARIO', 'Marathon Remote Imaging Observatory (MaRIO)'), ('NMS', 'New Mexico Skies'),
                         ('OES', 'Observatorio El Sauce'), ('PSA', 'PixelSkies'), ('REM', 'RemoteSkies.net'),
                         ('REMSG', 'Remote Skygems'), ('RLD', 'Riverland Dingo Observatory'), ('ROBO', 'RoboScopes'),
                         ('SS', 'Sahara Sky'), ('SPVO', 'San Pedro Valley Observatory'),
                         ('SRO', 'Sierra Remote Observatories'), ('SRO2', 'Sky Ranch Observatory'),
                         ('SPOO', 'SkyPi Remote Observatory'), ('SLO', 'Slooh'), ('SSLLC', 'Stellar Skies LLC'),
                         ('TAIYUGE', 'TaiYuge Observatory'), ('TELI', 'Telescope Live'),
                         ('WTO', 'West Texas Observatory (WTO)'), ('YUNLING', 'Yunling Observatory'),
                         ('OTHER', 'None of the above')],
                help_text='Which remote hosting facility did you use to acquire data for this image?', max_length=8,
                null=True, verbose_name='Remote data source'
            ),
        ),
    ]
