from . import views
from django.urls import path

urlpatterns = [
    path("", views.get,name="get"),
    path("new", views.post,name="post"),
]
               
#djaneiro 