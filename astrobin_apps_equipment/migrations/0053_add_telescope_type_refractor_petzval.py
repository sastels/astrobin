# Generated by Django 2.2.24 on 2022-05-08 07:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('astrobin_apps_equipment', '0052_add_telescope_type_catadioptric_riccardi_honders'),
    ]

    operations = [
        migrations.AlterField(
            model_name='telescope',
            name='type',
            field=models.CharField(
                choices=[('REFRACTOR_ACHROMATIC', 'Refractor: achromatic'),
                         ('REFRACTOR_SEMI_APOCHROMATIC', 'Refractor: semi-apochromatic'),
                         ('REFRACTOR_APOCHROMATIC', 'Refractor: apochromatic'),
                         ('REFRACTOR_NON_ACHROMATIC_GALILEAN', 'Refractor: non-achromatic Galilean'),
                         ('REFRACTOR_NON_ACHROMATIC_KEPLERIAN', 'Refractor: non-achromatic Keplerian'),
                         ('REFRACTOR_SUPERACHROMAT', 'Refractor: superachromat'),
                         ('REFRACTOR_PETZVAL', 'Refractor: Petzval'),
                         ('REFLECTOR_DALL_KIRKHAM', 'Reflector: Dall-Kirkham'),
                         ('REFLECTOR_NASMYTH', 'Reflector: Nasmyth'),
                         ('REFLECTOR_RITCHEY_CHRETIEN', 'Reflector: Ritchey Chretien'),
                         ('REFLECTOR_GREGORIAN', 'Reflector: Gregorian'),
                         ('REFLECTOR_HERSCHELLIAN', 'Reflector: Herschellian'),
                         ('REFLECTOR_NEWTONIAN', 'Reflector: Newtonian'),
                         ('CATADIOPTRIC_ARGUNOV_CASSEGRAIN', 'Catadioptric: Argunov-Cassegrain'),
                         ('CATADIOPTRIC_KLEVTSOV_CASSEGRAIN', 'Catadioptric: Klevtsov-Cassegrain'),
                         ('CATADIOPTRIC_LURIE_HOUGHTON', 'Catadioptric: Lurie-Houghton'),
                         ('CATADIOPTRIC_MAKSUTOV', 'Catadioptric: Maksutov'),
                         ('CATADIOPTRIC_MAKSUTOV_CASSEGRAIN', 'Catadioptric: Maksutov-Cassegrain'),
                         ('CATADIOPTRIC_MODIFIED_DALL_KIRKHAM', 'Catadioptric: modified Dall-Kirkham'),
                         ('CATADIOPTRIC_SCHMIDT_CAMERA', 'Catadioptric: Schmidt camera'),
                         ('CATADIOPTRIC_SCHMIDT_CASSEGRAIN', 'Catadioptric: Schmidt-Cassegrain'),
                         ('CATADIOPTRIC_ACF_SCHMIDT_CASSEGRAIN', 'Catadioptric: ACF Schmidt-Cassegrain'),
                         ('CATADIOPTRIC_ROWE_ACKERMAN_SCHMIDT', 'Catadioptric: Rowe-Atkinson Schmidt astrograph'),
                         ('CATADIOPTRIC_RICCARDI_HONDERS', 'Catadioptric: Riccardi-Honders'),
                         ('CAMERA_LENS', 'Camera lens'), ('BINOCULARS', 'Binoculars')], max_length=64,
                verbose_name='Type'
            ),
        ),
        migrations.AlterField(
            model_name='telescopeeditproposal',
            name='type',
            field=models.CharField(
                choices=[('REFRACTOR_ACHROMATIC', 'Refractor: achromatic'),
                         ('REFRACTOR_SEMI_APOCHROMATIC', 'Refractor: semi-apochromatic'),
                         ('REFRACTOR_APOCHROMATIC', 'Refractor: apochromatic'),
                         ('REFRACTOR_NON_ACHROMATIC_GALILEAN', 'Refractor: non-achromatic Galilean'),
                         ('REFRACTOR_NON_ACHROMATIC_KEPLERIAN', 'Refractor: non-achromatic Keplerian'),
                         ('REFRACTOR_SUPERACHROMAT', 'Refractor: superachromat'),
                         ('REFRACTOR_PETZVAL', 'Refractor: Petzval'),
                         ('REFLECTOR_DALL_KIRKHAM', 'Reflector: Dall-Kirkham'),
                         ('REFLECTOR_NASMYTH', 'Reflector: Nasmyth'),
                         ('REFLECTOR_RITCHEY_CHRETIEN', 'Reflector: Ritchey Chretien'),
                         ('REFLECTOR_GREGORIAN', 'Reflector: Gregorian'),
                         ('REFLECTOR_HERSCHELLIAN', 'Reflector: Herschellian'),
                         ('REFLECTOR_NEWTONIAN', 'Reflector: Newtonian'),
                         ('CATADIOPTRIC_ARGUNOV_CASSEGRAIN', 'Catadioptric: Argunov-Cassegrain'),
                         ('CATADIOPTRIC_KLEVTSOV_CASSEGRAIN', 'Catadioptric: Klevtsov-Cassegrain'),
                         ('CATADIOPTRIC_LURIE_HOUGHTON', 'Catadioptric: Lurie-Houghton'),
                         ('CATADIOPTRIC_MAKSUTOV', 'Catadioptric: Maksutov'),
                         ('CATADIOPTRIC_MAKSUTOV_CASSEGRAIN', 'Catadioptric: Maksutov-Cassegrain'),
                         ('CATADIOPTRIC_MODIFIED_DALL_KIRKHAM', 'Catadioptric: modified Dall-Kirkham'),
                         ('CATADIOPTRIC_SCHMIDT_CAMERA', 'Catadioptric: Schmidt camera'),
                         ('CATADIOPTRIC_SCHMIDT_CASSEGRAIN', 'Catadioptric: Schmidt-Cassegrain'),
                         ('CATADIOPTRIC_ACF_SCHMIDT_CASSEGRAIN', 'Catadioptric: ACF Schmidt-Cassegrain'),
                         ('CATADIOPTRIC_ROWE_ACKERMAN_SCHMIDT', 'Catadioptric: Rowe-Atkinson Schmidt astrograph'),
                         ('CATADIOPTRIC_RICCARDI_HONDERS', 'Catadioptric: Riccardi-Honders'),
                         ('CAMERA_LENS', 'Camera lens'), ('BINOCULARS', 'Binoculars')], max_length=64,
                verbose_name='Type'
            ),
        ),
    ]
