
from django.urls import path
from .views import ItemList,Itemd
urlpatterns=[
    path("tc",ItemList.as_view(),name="tc"),
    path("dc/<int:pk>",Itemd.as_view(),name="dc")

]