from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Kantor
from departemens.models import Departemen
from rest_framework import status
from .serializers import KantorSerializer

class kantorsListView(APIView):
    def get(self, request):
        items = Kantor.objects.all()
        serializer = KantorSerializer(items, many=True)
        return Response(serializer.data)
    

    def post(self, request):
        serializer = KantorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class KantorsDetailView(APIView):
    def get_object (self, pk):
        try:
            return Kantor.objects.get(pk=pk)
        except Kantor.DoesNotExist:
            return None
     
    def get(self, request, pk):
        item = self.get_object(pk)
        if item :
            serializer = KantorSerializer(item)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)
   
    def put(self, request, pk):
        item = self.get_object(pk)
        if item :
            serializer = KantorSerializer(item, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    def delete(self, request, pk):
        item = self.get_object(pk)
        if item :
            item.delete()
            return Response(status=status.HTTP_204_NO_CONTENT, data={"message": "Kantor Deleted Successfully"})
        return Response(status=status.HTTP_404_NOT_FOUND)