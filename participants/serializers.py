from rest_framework import serializers
from participants.models import Participants, TestSending


class ParticipantsCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participants
        fields = '__all__'


class TestCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestSending
        fields = '__all__'
