from django.urls import path
from .views import itemList

urlpatterns =[
    path('', itemList, name='itemList' )
]