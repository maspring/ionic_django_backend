from rest_framework import serializers
from jsframework.models import Picture

class PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Picture