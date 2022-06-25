from rest_framework import serializers
from .models import Participant


class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant 
        fields = ('name', 'date_of_birth', 'phone_number', 'address', 'reference_number')

    def create(self, validated_data):
        instance = Participant.objects.create(**validated_data)
        instance.reference_number = instance.generate_reference_number()
        instance.save()
        return instance

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.date_of_birth = validated_data.get('date_of_birth', instance.date_of_birth)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.address = validated_data.get('address', instance.address)
        instance.save()
        return instance