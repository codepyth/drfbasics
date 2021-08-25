from django.shortcuts import render
from .serializers import *
from rest_framework import generics
from .models import *
# Create your views here.

class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer