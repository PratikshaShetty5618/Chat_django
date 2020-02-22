from django.urls import path,include
from . import views
from rest_framework import routers
from django.conf.urls import include,url

router = routers.DefaultRouter()
router.register(r'users', views.UsersViewSet)
router.register(r'chats', views.ChatsViewSet)

urlpatterns=[
	path("",include(router.urls)),
	path("login/<int:key>/",views.login,name='login'),
	path("logout/",views.logout,name='logout'),

	
]