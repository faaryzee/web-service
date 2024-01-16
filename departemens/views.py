from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import  Departemen
from .serializers import  DepartemenSerializer

class DepartemenList(APIView):
    def get(self, request):
        DepartemenList = Departemen.objects.all()
        serializer = DepartemenSerializer(DepartemenList, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DepartemenSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CategoryDetil(APIView):
    def get_object(self, pk):
        try:
            return Departemen.objects.get(pk=pk)
        except Departemen.DoesNotExist:
            return None
   
    def get(self, request, pk):
        category = self.get_object(pk)
        if category :
            serializer = DepartemenSerializer(category)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)
   
    def put(self, request, pk):
        departemen = self.get_object(pk)
        if departemen :
            serializer = DepartemenSerializer(departemen, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_404_NOT_FOUND)
    

    def delete(self, request, pk):
        departemen = self.get_object(pk)
        if departemen :
            departemen.delete()
            return Response(status=status.HTTP_204_NO_CONTENT, data={"message": "Departemen Deleted Successfully"})
        return Response(status=status.HTTP_404_NOT_FOUND)