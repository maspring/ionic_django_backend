from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from jsframework.api.serializers.image_serializer import PictureSerializer
from jsframework.models import Picture

class PictureView(ListCreateAPIView):
    serializer_class = PictureSerializer

    def get(self, request):
        picture = Picture.objects.all()
        serializer = PictureSerializer(picture, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = PictureSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
