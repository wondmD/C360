from rest_framework import serializers
from resource.models import *
from main.models import *

class courseserializer (serializers.ModelSerializer):
    class Meta:
        model = myusers
        fields = '__all__'

