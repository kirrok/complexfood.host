# coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse
from main_app.models import *
from django.http import HttpResponseRedirect
from django import forms


class checkout_form(forms.Form):
    first_name = forms.CharField(label='Имя*', max_length=100)
    second_name = forms.CharField(label='Фамилия*', max_length=100)
    phone = forms.CharField(label='Телефон*', max_length=20)
    email = forms.EmailField(label='Email', max_length=50)
    street = forms.CharField(label='Улица*', max_length=100)
    house = forms.CharField(label='Дом*', max_length=12)
    housing = forms.CharField(required=False, label='Корпус', max_length=12)
    building = forms.CharField(required=False, label='Строение', max_length=12)
    entrance = forms.CharField(label='Подъезд*', max_length=12)
    floor = forms.CharField(label='Этаж*', max_length=12)
    room = forms.CharField(label='Квартира/Офис*', max_length=12)

    def __init__(self, *args, **kwargs):
        super(checkout_form, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'placeholder': 'Имя', 'required': ""})
        self.fields['second_name'].widget.attrs.update({'placeholder': 'Фамилия', 'required': ""})
        self.fields['phone'].widget.attrs.update({'placeholder': '+7', 'required': ""})
        self.fields['street'].widget.attrs.update({'placeholder': 'Улица*', 'required': ""})
        self.fields['house'].widget.attrs.update({'placeholder': 'Дом', 'required': ""})
        self.fields['housing'].widget.attrs.update({'placeholder': 'Корп.'})
        self.fields['building'].widget.attrs.update({'placeholder': 'Стр.'})
        self.fields['entrance'].widget.attrs.update({'placeholder': 'Подъезд', 'required': ""})
        self.fields['floor'].widget.attrs.update({'placeholder': 'Этаж', 'required': ""})
        self.fields['room'].widget.attrs.update({'placeholder': 'Квартира', 'required': ""})
        self.fields['email'].widget.attrs.update({'placeholder': 'example@email.com', 'required': ""})

        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'data-input'})


class feedback_form(forms.Form):
    first_name = forms.CharField(label='Имя*', max_length=100)
    email = forms.EmailField(label='Email*', max_length=50)
    topic = forms.CharField(required=False, label='Тема', max_length=100)
    letter = forms.CharField(widget=forms.Textarea, label='Сообщение')

    def __init__(self, *args, **kwargs):
        super(feedback_form, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'class': 'data-input', 'required': ""})
        self.fields['email'].widget.attrs.update({'class': 'data-input', 'required': ""})
        self.fields['topic'].widget.attrs.update({'class': 'data-input'})
        self.fields['letter'].widget.attrs.update({'class': 'text_area', 'required': ""})


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
    return render(request, 'order.html')


def learn_more(request):
    return render(request, 'learn_more.html')


def faq(request):
    return render(request, 'faq.html')


def feedback(request):
    if request.method == 'POST':
        form = feedback_form(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('thanks_feedback')

    else:
        form = feedback_form()
        return render(request, 'feedback.html', {'form': form})


def contacts(request):
    return render(request, 'contacts.html')


# Create your views here.

def checkout(request, id_, days_):
    if request.method == 'POST':
        form = checkout_form(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('thanks' + str(id_) + str(days_))

    else:
        form = checkout_form()
        set_ = set.objects.get(pk=id_)
        price_ = set_.calculate_price_for(int(days_))
        return render(request, 'order.html', {'form': form, 'id': id_, 'days': days_, 'set': set_, 'price': price_})


def thanks(request, id_=-1, days_=-1):
    if id_ != -1:
        set_ = set.objects.get(pk=id_)
        return render(request, 'thanks.html', {'set': set_, 'days': days_})
    else:
        return render(request, 'thanks_feedback.html')
