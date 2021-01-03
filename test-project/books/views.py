from django.shortcuts import render
from .serializers import *
from rest_framework import viewsets,permissions
from django.http import JsonResponse
from rest_framework.decorators import action

# Create your views here.

class BookViewSet(viewsets.ModelViewSet):

    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = Book.objects.all()
        return queryset

    @action(detail=False)     
    def search(self,request):
        search_input = self.request.data
        result = Book.objects.filter(name__icontains=search_input['name'])
        data_json = list(result.values())
        return JsonResponse({'Book Matches': data_json})
       

                        
