from django.shortcuts import render, HttpResponse
from django.views.generic import View

# Create your views here.
class Prueba(View):
		def get(self,request):
			return HttpResponse('Hola.')