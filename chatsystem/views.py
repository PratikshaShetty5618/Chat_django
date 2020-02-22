from rest_framework import viewsets
from django.shortcuts import render, get_object_or_404,redirect
from django.views.generic import CreateView, TemplateView
from django.http import HttpResponseRedirect,HttpResponse
from .serializers import LoginSerializer, ChatsSerializer
from .models import Login,Chats
from django.views.generic import CreateView, UpdateView


# Create your views here.
def check(request):
	try:
		request.session['login']
		request.session['user_id']
	except:
		request.session['login']=False
		request.session['user_id'] = 0
	return request.session['login']

def home(request):
	try:
		user_id = request.session['user_id'];
		user_address = Login.objects.filter(id = user_id)[0].public_address
		return render(request,'chatsystem/home.html',{'login':check(request),'user_address':user_address})
	except:
		return render(request,'chatsystem/home.html',{'login':check(request),'user_address':0})

class UsersViewSet(viewsets.ModelViewSet):
    queryset = Login.objects.all()
    serializer_class = LoginSerializer

class ChatsViewSet(viewsets.ModelViewSet):
    queryset = Chats.objects.all()
    serializer_class = ChatsSerializer

def login(request,key):
	if request.method != 'POST':
		raise Http404('Only POSTs are allowed')
	try:
		request.session['login'] = True
		request.session['user_id'] = key
		return HttpResponse("You're logged in.")
	except:
		return HttpResponse("Your username and password didn't match.")

def logout(request):
    try:
        del request.session['login']
        del request.session['user_id']
    except KeyError:
        pass
    return redirect('home')

# from django.shortcuts import render
# from .models import Auction
# # Create your views here.
# def index(request):
#     auctions = Auction.objects.all()
#     return render(request, 'website/index.html', {'auctions': auctions})

# def bid_page(request, auction_id):
#     return index(request)

# def comment(request, auction_id):
#     return index(request)

# def raise_bid(request, auction_id):

#    return bid_page(request, auction_id)

# def register_page(request):

#    return render(request, 'register.html')

# def watchlist(request, auction_id):

#    return index(request)

# def watchlist_page(request):

#    return index(request)

# def balance(request):

#    return index(request)

# def topup(request):

#    return index(request)

# def filter_auctions(request, category):

#    return index(request)

# def register(request):

#    return index(request)

# def login_page(request):

#    return index(request)

# def logout_page(request):

#    return index(request)