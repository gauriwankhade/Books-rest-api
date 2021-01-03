from django.shortcuts import render
from .serializers import *
from rest_framework import viewsets,permissions
from django.http import JsonResponse
from rest_framework.decorators import action
from rest_framework import filters

# Create your views here.

class BookViewSet(viewsets.ModelViewSet):

    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'url']

    def get_queryset(self):
        queryset = Book.objects.all()
        return queryset

    