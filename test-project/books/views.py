from django.shortcuts import render
from .serializers import *
from rest_framework import viewsets,permissions
from django.http import JsonResponse,HttpResponse
from rest_framework.decorators import action
from rest_framework import filters
from django.core.serializers import serialize
from rest_framework.response import Response
from .tasks import upadte_download
# Create your views here.

class BookViewSet(viewsets.ModelViewSet):

    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'url']

    def get_queryset(self):
        queryset = Book.objects.all()
        return queryset

    @action(detail=True)     
    def download(self,request,**kwargs):
        # pk = self.kwargs.get('pk')
        # book = Book.objects.get(pk=pk)  

        # if not book.is_downloaded:         
        #     task = upadte_download.delay(book.id)           
        #     return Response("Added to Downloads")
        
        # return Response("Downloaded..")

        task = upadte_download.delay()           
        return Response("Added to Downloads")