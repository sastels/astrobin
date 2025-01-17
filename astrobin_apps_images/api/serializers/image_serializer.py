from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from astrobin.api2.serializers.accessory_serializer import AccessorySerializer
from astrobin.api2.serializers.camera_serializer import CameraSerializer
from astrobin.api2.serializers.filter_serializer import FilterSerializer
from astrobin.api2.serializers.focal_reducer_serializer import FocalReducerSerializer
from astrobin.api2.serializers.mount_serializer import MountSerializer
from astrobin.api2.serializers.software_serializer import SoftwareSerializer
from astrobin.api2.serializers.telescope_serializer import TelescopeSerializer
from astrobin.models import DeepSky_Acquisition, Image, SolarSystem_Acquisition
from astrobin_apps_equipment.api.serializers.accessory_serializer import AccessorySerializer as AccessorySerializer2
from astrobin_apps_equipment.api.serializers.camera_serializer import CameraSerializer as CameraSerializer2
from astrobin_apps_equipment.api.serializers.filter_serializer import FilterSerializer as FilterSerializer2
from astrobin_apps_equipment.api.serializers.mount_serializer import MountSerializer as MountSerializer2
from astrobin_apps_equipment.api.serializers.software_serializer import SoftwareSerializer as SoftwareSerializer2
from astrobin_apps_equipment.api.serializers.telescope_serializer import TelescopeSerializer as TelescopeSerializer2
from astrobin_apps_images.api.fields import KeyValueTagsSerializerField
from astrobin_apps_images.api.serializers.deep_sky_acquisition_serializer import DeepSkyAcquisitionSerializer
from astrobin_apps_images.api.serializers.solar_system_acquisition_serializer import SolarSystemAcquisitionSerializer


class ImageSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    hash = serializers.PrimaryKeyRelatedField(read_only=True)
    w = serializers.IntegerField()
    h = serializers.IntegerField()
    uploader_in_progress = serializers.NullBooleanField(read_only=True)
    key_value_tags = KeyValueTagsSerializerField(source='keyvaluetags')

    imaging_telescopes = TelescopeSerializer(many=True, read_only=True)
    imaging_cameras = CameraSerializer(many=True, read_only=True)
    guiding_telescopes = TelescopeSerializer(many=True, read_only=True)
    guiding_cameras = CameraSerializer(many=True, read_only=True)
    focal_reducers = FocalReducerSerializer(many=True, read_only=True)
    mounts = MountSerializer(many=True, read_only=True)
    filters = FilterSerializer(many=True, read_only=True)
    accessories = AccessorySerializer(many=True, read_only=True)
    software = SoftwareSerializer(many=True, read_only=True)

    imaging_telescopes_2 = TelescopeSerializer2(many=True, required=False)
    imaging_cameras_2 = CameraSerializer2(many=True, required=False)
    guiding_telescopes_2 = TelescopeSerializer2(many=True, required=False)
    guiding_cameras_2 = CameraSerializer2(many=True, required=False)
    mounts_2 = MountSerializer2(many=True, required=False)
    filters_2 = FilterSerializer2(many=True, required=False)
    accessories_2 = AccessorySerializer2(many=True, required=False)
    software_2 = SoftwareSerializer2(many=True, required=False)

    deep_sky_acquisitions = DeepSkyAcquisitionSerializer(many=True, required=False, read_only=True)
    solar_system_acquisitions = SolarSystemAcquisitionSerializer(many=True, required=False, read_only=True)

    video_file = serializers.FileField(required=False, allow_null=True, read_only=True)
    encoded_video_file = serializers.FileField(required=False, allow_null=True, read_only=True)

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)

    def to_representation(self, instance: Image):
        representation = super().to_representation(instance)
        representation.update({
            'thumbnails': [
                {
                    'alias': alias,
                    'id': instance.pk,
                    'revision': 'final',
                    'url': instance.thumbnail(alias, None, sync=True)
                } for alias in ('gallery', 'story', 'regular', 'hd', 'qhd')
            ]
        })
        representation.update(self.acquisitions_representation(instance))
        return representation

    @staticmethod
    def acquisitions_representation(instance: Image):
        return {
            'deep_sky_acquisitions': DeepSkyAcquisitionSerializer(
                DeepSky_Acquisition.objects.filter(image=instance), many=True
            ).data,
            'solar_system_acquisitions': SolarSystemAcquisitionSerializer(
                SolarSystem_Acquisition.objects.filter(image=instance), many=True
            ).data
        }

    def validate_collaborators(self, collaborators):
        if collaborators and self.initial_data.get('user') in [x.id for x in collaborators]:
            raise ValidationError("Please do not include the image's user as a collaborator")

        return collaborators

    class Meta:
        model = Image
        fields = (
            'user',
            'collaborators',
            'pk',
            'hash',
            'title',
            'is_wip',
            'skip_notifications',
            'w',
            'h',
            'imaging_telescopes',
            'imaging_cameras',
            'guiding_telescopes',
            'guiding_cameras',
            'focal_reducers',
            'mounts',
            'filters',
            'accessories',
            'software',
            'imaging_telescopes_2',
            'imaging_cameras_2',
            'guiding_telescopes_2',
            'guiding_cameras_2',
            'mounts_2',
            'filters_2',
            'accessories_2',
            'software_2',
            'published',
            'license',
            'description',
            'description_bbcode',
            'link',
            'link_to_fits',
            'acquisition_type',
            'deep_sky_acquisitions',
            'solar_system_acquisitions',
            'subject_type',
            'solar_system_main_subject',
            'data_source',
            'remote_source',
            'part_of_group_set',
            'mouse_hover_image',
            'allow_comments',
            'uploader_in_progress',
            'square_cropping',
            'watermark',
            'watermark_text',
            'watermark_position',
            'watermark_size',
            'watermark_opacity',
            'sharpen_thumbnails',
            'key_value_tags',
            'locations',
            'full_size_display_limitation',
            'download_limitation',
            'loop_video',
            'video_file',
            'encoded_video_file',
        )
