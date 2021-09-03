from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import LoginView,Indexview,cartsView,ProductDetail,RemoveCartview,Addtocart,ViewOrder,CancelOrder

urlpatterns=[
    path("log",LoginView.as_view(),name="log"),
    path("in",Indexview.as_view(),name="in"),
    path("ca",cartsView.as_view(),name="ca"),
    path("pd/<int:pk>",ProductDetail.as_view(),name="pd"),
    path("ro/<int:pk>",RemoveCartview.as_view(),name="ro"),
    path("ac/<int:id>",Addtocart.as_view(),name="ac"),
    path("vo",ViewOrder.as_view(),name="vo"),
    path("co/<int:id>",CancelOrder.as_view(),name="co")
]

