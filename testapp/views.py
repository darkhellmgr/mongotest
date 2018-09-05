import json

from django.contrib.auth.models import User
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.

from .models import BlogPost, Entry


def index(request):
    x = Entry.objects.all()
    for i in x:
        m=i._id
    return HttpResponse(m)