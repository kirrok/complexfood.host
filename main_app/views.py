# coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse
from main_app.models import *
from django.http import HttpResponseRedirect
from django import forms
import math

class PFCForm(forms.Form):
    SEX_CHOISES = (('w', 'woman'), ('m', 'man'))
    ACTIVITY_CHOISES = (
        ('1', 'раз в неделю'),
        ('2', 'два раза в неделю'),
        ('3', 'три раза в неделю')
    )
    sex = forms.ChoiceField(label='Пол', widget=forms.RadioSelect, choices=SEX_CHOISES)
    age = forms.IntegerField(label='Возраст', min_value=10, max_value=100)
    weight = forms.IntegerField(label='Вес', widget=forms.TextInput)
    height = forms.IntegerField(label='Рост', widget=forms.TextInput)
    waist = forms.IntegerField(label='Обьем талии', widget=forms.TextInput)
    activity_level = forms.ChoiceField(label='Уровень активности', choices=ACTIVITY_CHOISES)
    desired_weight = forms.IntegerField(label='Желаемый вес', widget=forms.TextInput)

    def __init__(self, *args, **kwargs):
        super(PFCForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'required': ""})


class OrderForm(forms.ModelForm):
    class Meta:
        model = OrderModel
        fields = '__all__'
        widgets = {
            'house': forms.widgets.TextInput,
            'housing': forms.widgets.TextInput,
            'building': forms.widgets.TextInput,
            'entrance': forms.widgets.TextInput,
            'floor': forms.widgets.TextInput,
            'room': forms.widgets.TextInput,
        }
        exclude = ['product_id', 'price', 'duration']

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        placeholders = ['Имя', 'Фамилия', 'Телефон', 'example@email.com', 'Улица', 'Дом', 'Корпус', 'Строение',
                        'Подъезд', 'Этаж', 'Квартира', 'Номер набора', 'Цена']
        x = 0
        for field in self.fields:
            if field != 'housing' and field != 'building':
                self.fields[field].widget.attrs.update(
                    {'class': 'data-input', 'required': "", 'placeholder': placeholders[x]})
            else:
                self.fields[field].widget.attrs.update({'class': 'data-input', 'placeholder': placeholders[x]})
            x += 1


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = FeedbackModel
        fields = '__all__'
        widgets = {'letter': forms.widgets.Textarea}

    def __init__(self, *args, **kwargs):
        super(FeedbackForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'class': 'data-input', 'required': ""})
        self.fields['email'].widget.attrs.update({'class': 'data-input', 'required': ""})
        self.fields['topic'].widget.attrs.update({'class': 'data-input'})
        self.fields['letter'].widget.attrs.update({'class': 'text_area', 'required': ""})


def calculate_pfc(sex, age, weight, height, waist, activity_level, desired_weight):
    if sex == 'm':
        fat_percent = (4.15 * waist - 0.082 * weight - 98.42) / weight
    else:
        fat_percent = (4.15 * waist - 0.082 * weight - 76.76) / weight

    lbm = weight * (100 - fat_percent)/100
    passive_metabolism = 370 + 21.6 * lbm

    if activity_level == '1':
        coefficient = 1.2
    elif activity_level == '2':
        coefficient = 1.275
    elif activity_level == '3':
        coefficient = 1.55
    elif activity_level == '4':
        coefficient = 1.725
    elif activity_level == '1.9':
        coefficient = 1.9

    activity_metabolism = passive_metabolism * coefficient

    return math.trunc(activity_metabolism)


def pfc(request):
    if request.method == 'POST':
        form = PFCForm(request.POST)
        if form.is_valid():
            sex = form.cleaned_data['sex']
            age = form.cleaned_data['age']
            weight = form.cleaned_data['weight']
            height = form.cleaned_data['height']
            waist = form.cleaned_data['waist']
            activity_level = form.cleaned_data['activity_level']
            desired_weight = form.cleaned_data['desired_weight']

            calorific_value = calculate_pfc(sex, age, weight, height, waist, activity_level, desired_weight)
            return render(request, 'PFC.html', {'result': calorific_value})

    else:
        form = PFCForm()
        return render(request, 'PFC.html', {'form': form})


def index(request):
    request.session["x"] = True
    return render(request, 'index.html')


def base(request):
    return render(request, 'base.html')


def menu(request):
    sets_ = SetModel.objects.all()
    return render(request, 'menu.html', {'sets': sets_})


def set_info(request, id_):
    set_ = SetModel.objects.get(pk=id_)
    ration_ = set_.ration.all()
    return render(request, 'set_info.html', {'set': set_, 'ration': ration_})


def learn_more(request):
    return render(request, 'learn_more.html')


def faq(request):
    return render(request, 'faq.html')


def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('thanks_feedback')

    else:
        form = FeedbackForm()
        return render(request, 'feedback.html', {'form': form})


def contacts(request):
    return render(request, 'contacts.html')


# Create your views here.

def checkout(request, id_, days_):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            product_ = SetModel.objects.get(pk=id_)
            price_ = product_.calculate_price_for(int(days_))

            order = form.save(commit=False)
            order.product_id = product_.id
            order.price = price_
            order.duration = days_

            order.save()
            return HttpResponseRedirect('thanks' + str(id_) + str(days_))

    else:
        form = OrderForm()
        set_ = SetModel.objects.get(pk=id_)
        price_ = set_.calculate_price_for(int(days_))
        return render(request, 'order.html', {'form': form, 'id': id_, 'days': days_, 'set': set_, 'price': price_})


def backend_orders(request):
    orders = OrderModel.objects.all()
    return render(request, 'backend_orders.html', {'orders': orders})


def thanks(request, id_=-1, days_=-1):
    if id_ != -1:
        set_ = SetModel.objects.get(pk=id_)
        return render(request, 'thanks.html', {'set': set_, 'days': days_})
    else:
        return render(request, 'thanks_feedback.html')
