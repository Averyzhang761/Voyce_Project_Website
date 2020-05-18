from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

from .forms import ContactForm


def index(request):
    return render(request, 'index.html')