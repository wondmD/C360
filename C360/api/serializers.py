from rest_framework import serializers
from resource.models import *

class courseserializer (serializers.ModelSerializer):
    class Meta:
        model = course
        fields = '__all__'

