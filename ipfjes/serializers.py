from rest_framework import serializers
from ipfjes.models import SocCode


class SocCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocCode
