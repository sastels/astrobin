# Generated by Django 2.2.24 on 2021-09-03 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('astrobin_apps_equipment', '0009_make_equipment_item_image_optional'),
    ]

    operations = [
        migrations.AlterField(
            model_name='camera',
            name='name',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='name',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='telescope',
            name='name',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterUniqueTogether(
            name='camera',
            unique_together={('brand', 'name')},
        ),
        migrations.AlterUniqueTogether(
            name='sensor',
            unique_together={('brand', 'name')},
        ),
        migrations.AlterUniqueTogether(
            name='telescope',
            unique_together={('brand', 'name')},
        ),
    ]
