from django.urls import path,include
from . import views
from rest_framework import routers
from django.conf.urls import include,url

router = routers.DefaultRouter()
router.register(r'users', views.AuctionViewSet)

urlpatterns=[
	path("",include(router.urls)),	
]