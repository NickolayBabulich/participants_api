from django.urls import path
from participants.views import ParticipantsCreateAPIView

urlpatterns = [
    path('participants/create/', ParticipantsCreateAPIView.as_view(), name='participants-create'),
]