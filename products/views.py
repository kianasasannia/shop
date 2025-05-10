from django.shortcuts import render
from django.http import HttpResponse

def home (resquests):
    return HttpResponse("<h1>به فروشگاه ما خوش آمدید </h1>")
