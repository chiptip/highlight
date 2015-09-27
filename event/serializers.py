from event.models import Event
from rest_framework import serializers


class EventSerializer(serializers.ModelSerializer):

    url = serializers.CharField(style={'base_template': 'textarea.html'})

    def get_event_url(self, obj):
        return obj.event.url

    class Meta:
        model = Event
        fields = ('id', 'url')
        read_only_fields = ('id')
