from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Game, Person


# Create your views here.

def index(request):

    return render(request, 'blogApp/index.html')