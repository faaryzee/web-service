from rest_framework import serializers
from .models import Kantor
from karyawans.serializers import karyawanSerializer
from departemens.serializers import DepartemenSerializer

class KantorSerializer(serializers.ModelSerializer):
    karyawan = karyawanSerializer(many=True, read_only=True)
    # departemen = DepartemenSerializer(many=True, read_only=True)
    class Meta:
        model = Kantor
        fields = ['id', 'title', 'lokasi', 'departemen', 'karyawan']