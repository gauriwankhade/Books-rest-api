from django.shortcuts import render
from .serializers import *
from rest_framework import viewsets,permissions
from django.http import JsonResponse,HttpResponse
from rest_framework.decorators import action
from rest_framework import filters
from django.core.serializers import serialize
from rest_framework.response import Response
import urllib.request
from django.core.files.base import ContentFile

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
        pk = self.kwargs.get('pk')
        book = Book.objects.get(pk=pk)
        # print(book[0].url)
        # data = serialize("json", book)
        # return HttpResponse(data, content_type="application/json")
       
        
        my_request = urllib.request.urlopen("https://www.amazon.in/Silent-Patient-Alex-Michaelides/dp/1409181634/ref=sr_1_1?crid=9Y0O67849KZ1&dchild=1&keywords=silent+patient&qid=1609664261&s=books&sprefix=silent+%2Caps%2C325&sr=1-1")
        my_HTML = my_request.read().decode("utf8")
        print(my_HTML)

        updated_file = ContentFile(my_HTML)
        updated_file.name = "{book_name}.html".format(book_name=book.name)

        book.downloaded_file = updated_file
        book.save()

        return Response("hello1")
        
    