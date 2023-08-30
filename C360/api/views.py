from rest_framework.response import Response
from rest_framework.decorators import api_view
from resource.models import *
from .serializers import courseserializer

@api_view(['GET'])
def getData(request):
    courses = course.objects.all()
    serializer = courseserializer(courses, many=True)
    return Response(serializer.data)
