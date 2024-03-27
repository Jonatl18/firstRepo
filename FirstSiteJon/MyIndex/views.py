from django.shortcuts import render
from django.http import HttpResponse


def MyIndex(request):
    return render(request, 'index.html')