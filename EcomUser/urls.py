from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import LoginView,Indexview,cartsView,ProductDetail,RemoveCartview,Addtocart,ViewOrder,CancelOrder,OrderPro

urlpatterns=[
    path("login",LoginView.as_view(),name="log"),
    path("index",Indexview.as_view(),name="in"),
    path("cart",cartsView.as_view(),name="ca"),
    path("productdetail/<int:pk>",ProductDetail.as_view(),name="pd"),
    path("removecart/<int:pk>",RemoveCartview.as_view(),name="ro"),
    path("addtocart/<int:id>",Addtocart.as_view(),name="ac"),
    path("vieworder",ViewOrder.as_view(),name="vo"),
    path("cancelorder/<int:id>",CancelOrder.as_view(),name="co"),
    path("orderproduct",OrderPro.as_view(),name="op")
]


