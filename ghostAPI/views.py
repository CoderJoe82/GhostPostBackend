from rest_framework import viewsets
from ghostAPI import models, serializers


class GhostPost_view(viewsets.ModelViewSet):

    queryset = models.GhostPost.objects.all()
    serializer_class = serializers.ghostpost_serializer