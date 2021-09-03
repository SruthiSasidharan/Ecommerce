from rest_framework import mixins
from rest_framework import generics
from rest_framework.views import APIView

from .models import Category,Items
from .serializers import Itemserializer
from EcomUser.serializers import OrderSerializer
from .models import Orders

class ItemList(generics.ListCreateAPIView):
    queryset = Items.objects.all()
    serializer_class = Itemserializer

class Itemd(generics.RetrieveUpdateDestroyAPIView):
    queryset = Items.objects.all()
    serializer_class = Itemserializer


class OrderView(generics.ListAPIView):
        queryset = Orders.objects.all()
        serializer_class =OrderSerializer
