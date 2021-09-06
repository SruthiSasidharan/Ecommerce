from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import LoginView,Indexview,cartsView,ProductDetail,RemoveCartview,Addtocart,ViewOrder,CancelOrder,OrderPro

urlpatterns=[
    path("login",LoginView.as_view(),name="User login"),
    path("index",Indexview.as_view(),name="Index page"),
    path("productdetail/<int:pk>",ProductDetail.as_view(),name="detailed view of a product"),
    path("addtocart/<int:id>",Addtocart.as_view(),name="add a product to cart"),
    path("cart",cartsView.as_view(),name="Cart page"),
    path("removecart/<int:pk>",RemoveCartview.as_view(),name="remove product from cart"),
    path("orderproduct", OrderPro.as_view(), name="to order a product"),
    path("vieworder",ViewOrder.as_view(),name="view orders"),
    path("cancelorder/<int:id>",CancelOrder.as_view(),name="cancel an order"),

]


