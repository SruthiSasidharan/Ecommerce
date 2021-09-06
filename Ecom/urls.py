
from django.urls import path
from .views import ItemList,Itemd,OrderView
urlpatterns=[
    path("itemlist",ItemList.as_view(),name="tc"),
    path("itemdetails/<int:pk>",Itemd.as_view(),name="dc"),
    path("orderview",OrderView.as_view(),name="ov")

]