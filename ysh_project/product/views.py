from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def product_list(request):
    return HttpResponse('product_list test success')

def product_detail(requset, product_id):
    return HttpResponse('product_detail test success')