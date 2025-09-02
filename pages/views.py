from django.shortcuts import render
from django.http import HttpResponse

def	homePageViews(request):
	return HttpResponse('Hello word!')

