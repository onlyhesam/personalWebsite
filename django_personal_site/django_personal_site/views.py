


from django import template
from django.http.response import HttpResponse
# from django.template import loader
from django.shortcuts import render





def index(request):
    return render(request,  'index.html')


def blogPost1(request):
    return render(request,  'blog-post-1.html')



