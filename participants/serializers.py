from rest_framework import serializers
from participants.models import Participants


class ParticipantsCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participants
        fields = '__all__'
