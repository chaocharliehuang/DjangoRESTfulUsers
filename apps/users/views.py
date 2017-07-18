from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages

def index(request):
    return HttpResponse('hello world')