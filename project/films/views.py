from django.shortcuts import render
from django.http import HttpResponse # added
# Create your views here.
def home(request):
	return render(request, 'home.html')
	
def main(request):
	return render(request, 'films/main.html')

def user_info(request):
	return render(request, 'films/user_info.html')