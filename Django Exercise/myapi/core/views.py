from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from core.serializers import StudentSerializer

# Create your views here.
class HelloView(APIView):
    permission_classes = (IsAuthenticated,)
    #def get(self, request):
    #    content = {'message': 'Hello, World!'}
    #    return Response(content)

    def post(self, request, *args, **kwargs):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)