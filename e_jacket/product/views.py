from django.shortcuts import render
from django.http import Http404
from .serializers import *
from rest_framework.views import APIView
from .models import *
from rest_framework.response import Response


# Create your views here.
class LatestProductList(APIView):
  def get(self, request , format=None):
    products = Product.objects.all()[0:4]
    serializer = ProductSerializer(products,many = True)
    return Response(serializer.data)

class ProductDetail(APIView):
  def get_object(self,category_slug,product_slug):
    try:
      return Product.objects.filter(category__slug=category_slug).get(slug=product_slug)
    except Product.DoesNotExist:
      raise Http404

  def get(self,request,category_slug,product_slug):
    product = self.get_object(category_slug,product_slug)
    serializers = ProductSerializer(product)
    return Response(serializers.data)
