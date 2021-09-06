
from django.urls import path
from .views import ItemList,Itemd,OrderView
urlpatterns=[
    path("addProduct",ItemList.as_view(),name="To add an item"),
    path("itemDetailes/<int:pk>",Itemd.as_view(),name="to retrive,update and delete product"),
    path("orderview",OrderView.as_view(),name="To view all orders")

]