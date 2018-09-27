from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
	return HttpResponse("My firsr Django app")

#Template..
def search_book(request):
	return render(request,'searchform.html')

def book_response(request):
	if 'q' in request.GET:
		msg='you searched for : %r' % request.GET['q']
	else:
		msg='empty request >>'

	return HttpResponse(msg)