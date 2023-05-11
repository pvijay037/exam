from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from api.models import Event
from api.serializers import EventSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    @action(detail=False, methods=['get'])
    def latest_events(self, request):
        limit = int(request.query_params.get('limit', 5))
        page = int(request.query_params.get('page', 1))

        start_index = (page - 1) * limit
        end_index = start_index + limit

        events = Event.objects.order_by('-schedule')[start_index:end_index]
        serializer = self.get_serializer(events, many=True)

        return Response(serializer.data)


