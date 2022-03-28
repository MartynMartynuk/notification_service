from rest_framework.serializers import ModelSerializer
from service.models import *


class MailingListSerializer(ModelSerializer):
    class Meta:
        model = MailingList
        fields = '__all__'


class ClientSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

    def create(self, validated_data):
        return Client.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.phone = validated_data.get('phone', instance.phone)
        instance.operator_code = validated_data.get('operator_code', instance.operator_code)
        instance.tag = validated_data.get('tag', instance.tag)
        instance.timezone = validated_data.get('timezone', instance.timezone)
        instance.save()
        return instance
