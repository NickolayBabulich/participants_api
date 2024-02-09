from rest_framework import generics
from rest_framework.status import HTTP_200_OK
from participants.models import Participants, TestSending
from participants.serializers import ParticipantsCreateSerializer, TestCreateSerializer
from rest_framework.response import Response
from django.shortcuts import render


class ParticipantsCreateAPIView(generics.CreateAPIView):
    queryset = Participants.objects.all()
    serializer_class = ParticipantsCreateSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response({
            'status': HTTP_200_OK,
            'created': True
        })
    #
    # def get(self, request):
    #     return render(request, 'participants/empty.html')


class TestCreateAPIView(generics.CreateAPIView):
    queryset = Participants.objects.all()
    serializer_class = TestCreateSerializer
