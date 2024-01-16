from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from kantors.models import Kantor
from .models import Review
from .serializers import karyawanSerializer  # Sesuaikan dengan nama file serializer yang benar

class KaeyanwanView(APIView):
    def get(self, request):
        review = Review.objects.all()
        serialize = karyawanSerializer(review, many=True)
        return Response(serialize.data)

    def post(self, request):
        serializer = karyawanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class DetailKaryawan(APIView):
    def get_object(self, pk):
        try:
            return Review.objects.get(pk=pk)
        except Review.DoesNotExist:
            return None
    
    def get(self, request, pk):
        review = self.get_object(pk)
        if review:
            serialize = karyawanSerializer(review)
            return Response(serialize.data)
        return Response(status=status.HTTP_404_NOT_FOUND)
   
    def put(self, request, pk):
        review = self.get_object(pk)
        if review :
            serializer = karyawanSerializer(review, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    def delete(self, request, pk):
        review = self.get_object(pk)
        if review :
            review.delete()
            return Response(status=status.HTTP_204_NO_CONTENT, data={"message": "Kantor Deleted Successfully"})
        return Response(status=status.HTTP_404_NOT_FOUND)
    