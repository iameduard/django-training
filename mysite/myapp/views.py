from django.shortcuts import render
import datetime
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Book
from .forms import ContactForm
from django.core.mail import send_mail, get_connection


# Create your views here.

def index(request):
	return HttpResponse("My firsr Django app")

#Template..
def search_book(request):
	return render(request,'searchform.html')

def book_response(request):
	errors=dict()
	if 'q' in request.GET:
		q=request.GET['q']
		if not q:
			errors.append('Enter a search entry')
		elif len(q)>5:
			errors.append('Please enter at most 5 characters')
		else:
			books=Book.objects.get(Bookname=q)
			print('books ===== %s',books)
			return render(request,'searchresult.html',{'book':books,'query':q})

	return render(request,'searchform.html',{'error':errors})

def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			data=form.cleaned_data
			connect=get_connection('django.core.mail.backends.console.EmailBackend')
			send_mail(
				data['subject'],
				data['message'],
				data.get('email','ejimenmail@gmail.com'),
				['iameduard@hotmail.com'],connection=connect)
			return HttpResponseRedirect('/contact/thanks')
			#return HttpResponseRedirect('www.google.com')
	else:
		form = ContactForm(initial={'subject':'Django Training'})
		return render(request,'contact_form.html',{'form':form})

