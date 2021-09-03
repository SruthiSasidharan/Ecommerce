from rest_framework import mixins
from rest_framework import generics
from .models import Category,Items
from .serializers import Itemserializer


class ItemList(generics.ListCreateAPIView):
    queryset = Items.objects.all()
    serializer_class = Itemserializer

class Itemd(generics.RetrieveUpdateDestroyAPIView):
    queryset = Items.objects.all()
    serializer_class = Itemserializer


