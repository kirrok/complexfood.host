# coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse
from main_app.models import *
from django.http import HttpResponseRedirect
from django import forms


class checkout_form(forms.Form):
    first_name = forms.CharField(label='Имя', max_length=100)
    second_name = forms.CharField(label='Фамилия', max_length=100)
    phone = forms.CharField(label='Телефон', max_length=12)

    def __init__(self, *args, **kwargs):
        super(checkout_form, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'placeholder': 'Имя'})
        self.fields['second_name'].widget.attrs.update({'placeholder': 'Фамилия'})
        self.fields['phone'].widget.attrs.update({'placeholder': '+7'})
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'data-input'})



def index(request):
    return render(request, 'index.html')


def base(request):
    return render(request, 'base.html')


def menu(request):
    sets_ = set.objects.all()
    return render(request, 'menu.html', {'sets': sets_})


def set_info(request, id):
    set_ = set.objects.get(pk=id)
    ration_ = set_.ration_set.all()
    return render(request, 'set_info.html', {'set': set_, 'ration': ration_})


def to_order(request):
    return render(request, 'decor.html')


def learn_more(request):
    return render(request, 'learn_more.html')


def checkout(request):
    return render(request, 'checkout.html')


def questions(request):
    return render(request, 'questions.html')


def feedback(request):
    return render(request, 'feedback.html')


def contacts(request):
    return render(request, 'contacts.html')


# Create your views here.

def checkout(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = checkout_form(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('thanks')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = checkout_form()

    return render(request, 'decor.html', {'form': form})


def thanks(request):
    return render(request, 'thanks.html')
