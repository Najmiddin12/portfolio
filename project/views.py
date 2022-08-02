from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.views import View
from .models import Card, App, Web, Teammate


def contact(request):
    return render(request, "project/index.html")

def product(request):
    app = App.objects.all()
    card = Card.objects.all()
    web = Web.objects.all()
    teammate = Teammate.objects.all()

    return render(request, 'project/index.html', {"app": app, "card": card, "web": web, "teammate": teammate})

def app_detail(request, pk):
    app_dt = App.objects.get(pk=pk)

    return render(request, 'project/app-details.html', {"app_dt": app_dt})

def card_detail(request, pk):
    card_dt = Card.objects.get(pk=pk)

    return render(request, 'project/card-details.html', {"card_dt": card_dt})

def web_detail(request, pk):
    web_dt = Web.objects.get(pk=pk)

    return render(request, 'project/web-details.html', {"web_dt": web_dt})
