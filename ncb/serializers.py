from rest_framework import serializers

from theme.models import MasterNCB


class MasterNCBSerializer(serializers.ModelSerializer):
    class Meta:
        model = MasterNCB
        fields = ['id', 'name', 'description', 'status']
