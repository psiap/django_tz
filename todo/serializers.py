from rest_framework import serializers
from .models import Client, DealsFile

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"


class DealsFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = DealsFile
        fields = "__all__"