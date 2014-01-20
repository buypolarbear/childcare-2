from rest_framework import routers, viewsets
from childcare.apps.progress.models import Activity


class ActivityViewSet(viewsets.ModelViewSet):
    model = Activity