from django.urls import path
from .views import homePageview

urlpatterns = [
	path('',homePageView, name = 'home');
]
