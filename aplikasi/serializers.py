from rest_framework import serializers, viewsets

from .models import Aplikasi


class AplikasiSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Aplikasi
        fields = (
            'name',
        )


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Aplikasi.objects.all()
    serializer_class = AplikasiSerializer
