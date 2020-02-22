from rest_framework import viewsets
from django.shortcuts import render, get_object_or_404,redirect
from django.views.generic import CreateView, TemplateView
from django.http import HttpResponseRedirect,HttpResponse
from .serializers import AuctionSerializer
from .models import Auction
from django.views.generic import CreateView, UpdateView
# Create your views here.
class AuctionViewSet(viewsets.ModelViewSet):
    queryset = Auction.objects.all()
    serializer_class = AuctionSerializer

def auction_button(request):
	return render(request,'auction/auction_button.html',{})

def create_artwork(request):
	return render(request,'auction/create_artwork.html',{})

def auction_list(request):
	auction = Auction.objects.all()
	return render(request,'auction/auction_list.html',{'auction':auction})

def auction_detail(request,pk):
	auction = get_object_or_404(Auction,pk=pk)
	return render(request,'auction/auction_detail.html',{'auction':auction})