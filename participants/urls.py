from django.urls import path
from participants.views import ParticipantsCreateAPIView, TestCreateAPIView

urlpatterns = [
    path('participants/create/', ParticipantsCreateAPIView.as_view(), name='participants-create'),
    path('test/create/', TestCreateAPIView.as_view(), name='test-create'),
]