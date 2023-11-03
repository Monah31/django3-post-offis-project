from rest_framework import serializers
from .models import Letters
from rest_framework.renderers import JSONRenderer


class LettersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Letters
        fields = "__all__"

    # senders_name = serializers.CharField(max_length=128)
    # receiver_name = serializers.CharField(max_length=128)
    # point_of_departure = serializers.CharField()
    # pick_up_piont = serializers.CharField()
    # sender_index = serializers.IntegerField()
    # recipient_index = serializers.IntegerField()
    # mail_weight = serializers.IntegerField()
    # letter_type_id = serializers.IntegerField()

    # def create(self, validated_data):
    #     return Letters.objects.create(**validated_data)
    
    # def update(self, instance, validated_data):
    #     instance.senders_name = validated_data.get('senders_name', instance.senders_name)
    #     instance.receiver_name = validated_data.get('receiver_name', instance.receiver_name)
    #     instance.point_of_departure = validated_data.get('point_of_departure', instance.point_of_departure)
    #     instance.pick_up_piont = validated_data.get('pick_up_piont', instance.pick_up_piont)
    #     instance.sender_index = validated_data.get('sender_index', instance.sender_index)
    #     instance.recipient_index = validated_data.get('recipient_index', instance.recipient_index)
    #     instance.mail_weight = validated_data.get('mail_weight', instance.mail_weight)
    #     instance.receivletter_type_ider_name = validated_data.get('letter_type_id', instance.letter_type_id)
    #     instance.save()
    #     return instance
