"""chat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from chatsystem import views as chat_views
from auction import views as auction_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',chat_views.home,name='home'),
    path('auction_button/',auction_views.auction_button,name='auction_button'),
    path('create_artwork/',auction_views.create_artwork,name='create_artwork'),
    path('auction_list/',auction_views.auction_list,name='auction_list'),
    path('auction_detail/<int:pk>/',auction_views.auction_detail,name='auction_detail'),    
    path('chatsystem/',include('chatsystem.urls')),
    path('auction/',include('auction.urls')),
]

# from django.contrib import admin
# from django.urls import path, include
# from website import views as web_views

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', web_views.index, name='index'),
#     path('login/', web_views.login_page, name='login_view'),
#     path('logout/', web_views.logout_page, name='logout_view'),
#     path('register/', web_views.register_page, name='register_page'),
#     path('register/new_user/', web_views.register, name='register'),
#     path('category/<str:category>/', web_views.filter_auctions, name='filter_auctions'),
#     path('watchlist/<int:auction_id>/', web_views.watchlist, name='watchlist'),
#     path('balance/', web_views.balance, name='balance'),
#     path('balance/topup/', web_views.topup, name='topup'),
#     path('watchlist/', web_views.watchlist_page, name='watchlist'),
#     path('bid/<int:auction_id>/', web_views.bid_page, name='bid_page'),
#     path('bid/<int:auction_id>/comment/', web_views.comment, name='comment'),
#     path('bid/<int:auction_id>/raise_bid/', web_views.raise_bid, name='raise_bid'),
# ]