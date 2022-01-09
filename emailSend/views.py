from django.shortcuts import render,redirect
# from .models import UserData

# Create your views here.

def index(request):
    return redirect('/admin')
