from django.shortcuts import render

def home(request):
	return render(request,'home.html',{})
def about(request):
	return render(request,'about.html',{})
def blog(request):
	return render(request,'blog.html',{})
def blog_details(request):
	return render(request,'blog_details.html',{})
def contact(request):
	return render(request,'contact.html',{})
def pricing(request):
	return render(request,'pricing.html',{})
def service(request):
	return render(request,'service.html',{})
def home2(request):
	return render(request,'home.html',{})