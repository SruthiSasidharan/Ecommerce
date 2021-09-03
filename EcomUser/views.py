from .serializers import LoginSerializer,CartSerializer,OrderSerializer,AddToCartSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, authentication
from django.contrib.auth import authenticate,login
from rest_framework.authtoken.models import Token
from rest_framework import mixins
from rest_framework import generics
from Ecom.models import Items,Orders,Mycart
from rest_framework import permissions
from Ecom.serializers import Itemserializer

class LoginView(APIView):
     def post(self,request):
        serializer=LoginSerializer(data=request.data)
        if serializer.is_valid():
            username=serializer.validated_data.get("username")
            password=serializer.validated_data.get("password")
            user=authenticate(request,username=username,password=password)
            if user:
                login(request,user)
                token,created=Token.objects.get_or_create(user=user)
                return Response({"token": token.key})
            else:
                return Response({"msg":"invalid credential"})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
class Indexview(generics.GenericAPIView,
               mixins.ListModelMixin,mixins.CreateModelMixin):
    authentication_classes = [authentication.TokenAuthentication,authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    queryset = Items.objects.all()
    serializer_class = Itemserializer
    filterset_fields = ['title']
    def get(self,request,*args,**kwargs):
        return  self.list(request,*args,**kwargs)

# class Indexview(generics.ListCreateAPIView):
#     queryset = Items.objects.all()
#     serializer_class = Itemserializer

class ProductDetail(generics.RetrieveAPIView):
    queryset = Items.objects.all()
    serializer_class = Itemserializer

class Addtocart(APIView):
    def post(self,request,*args,**kwargs):
        pid=kwargs.get("id")
        items = Items.objects.get(id=pid)
        user = request.user
        cart = Mycart(product=items,user=user)
        cart.save()
        return Response(status=status.HTTP_200_OK)

class cartsView(generics.GenericAPIView,mixins.ListModelMixin):
    queryset = Mycart.objects.filter(status="cart")
    serializer_class = CartSerializer
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class RemoveCartview(generics.DestroyAPIView):
    queryset = Mycart.objects.all()
    serializer_class = CartSerializer

class ViewOrder(APIView):
    def get(self,request,*args,**kwargs):
         order=Orders.objects.filter(user=request.user)
         serializer = OrderSerializer(order, many=True)
         return Response(serializer.data, status=200)

class CancelOrder(APIView):
        def get(self, request, *args, **kwargs):
            id = kwargs.get("id")
            order = Orders.objects.get(id=id)
            order.status = "cancelled"
            order.save()
            return Response(status=status.HTTP_200_OK)

class OrderPro(APIView):
    queryset=Mycart.objects.all()
    def post(self, request, format=None):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

