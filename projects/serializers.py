from django.contrib.auth.models import User
from rest_framework import serializers, viewsets
from vendor.serializers import VendorSerializer
from .models import Task


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
        )


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    vendor = VendorSerializer(read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Task
        fields = (
            'number',
            'project_title',
            'vendor',
            'user',
            'register_date',
            'target_implement_date',
            'actual_implement_date',
            'state',
            'mandays',
            'remarks',
            'created_at',
        )


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
