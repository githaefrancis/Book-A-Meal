from http.client import HTTPResponse
from django.shortcuts import render

# Create your views here.
def menu(request):
  return HTTPResponse('hello')