from django.shortcuts import render
from django.http import HttpResponse
from main_app.models import *

def index(request):
	return render(request, 'index.html')

def base(request):
	return render(request, 'base.html')

def menu(request):
	sets_ = set.objects.all()
	return render(request, 'menu.html',{'sets': sets_})

def learn_more(request):
	return render(request, 'learn_more.html')

def questions(request):
	return render(request, 'questions.html')

def feedback(request):
	return render(request, 'feedback.html')

def contacts(request):
	return render(request, 'contacts.html')
# Create your views here.
