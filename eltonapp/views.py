from django.shortcuts import render
from .models import *
from django.urls import path


# Create your views here.
def index(request):
    imageGroup = ImageGroup.objects.all()
    images = Image.objects.all()
    context = {
        "images": images,
        "group": imageGroup,
    }
    return render(
        request,
        "index.html",
        context,
    )


def form(request):
    return render(
        request,
        "form.html",
    )
