
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import *

class TokenPairView(TokenObtainPairView):
      serializer_class = TokenPairSerializer

class AgendaViewset(viewsets.ModelViewSet):
    queryset =agenda.objects.all()
    serializer_class = AgendaSerializer

class ClubViewset(viewsets.ModelViewSet):
    queryset =Club.objects.all()
    serializer_class = ClubSerializer

class ClientViewset(viewsets.ModelViewSet):
    queryset= Client.objects.all()
    serializer_class = ClientSerializer

class VideoViewset(viewsets.ModelViewSet):
    queryset= Video.objects.all()
    serializer_class = VideoSerializer
    
class BookingViewset(viewsets.ModelViewSet):
    queryset= Booking.objects.all()
    serializer_class = BookingSerializer

