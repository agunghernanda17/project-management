from rest_framework import serializers, viewsets

from .models import Projects_status


class Projects_statusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project_status
        fields = (
            'name',
        )

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Projects_status.objects.all()
    serializer_class = Projects_statusSerializer
