from rest_framework.serializers import ModelSerializer
from service.models import *


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


class MailingListSerializer(ModelSerializer):
    class Meta:
        model = MailingList
        fields = '__all__'

    def create(self, validated_data):
        return MailingList.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.start_time = validated_data.get('start_time', instance.start_time)
        instance.message_text = validated_data.get('message_text', instance.message_text)
        instance.client_filter = validated_data.get('client_filter', instance.client_filter)
        instance.end_time = validated_data.get('end_time', instance.end_time)
        instance.save()
        return instance


class MessageSerializer(ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'

    def create(self, validated_data):
        return Message.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.time_create = validated_data.get('time_create', instance.time_create)
        instance.sending_status = validated_data.get('sending_status', instance.sending_status)
        instance.mailinglist_id = validated_data.get('mailinglist_id', instance.mailinglist_id)
        instance.client_id = validated_data.get('client_id', instance.client_id)
        instance.save()
        return instance