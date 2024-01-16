from rest_framework import serializers
from .models import Departemen

class DepartemenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departemen
        fields = ['id', 'name']