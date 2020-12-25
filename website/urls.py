from django.urls import path
from . import views

urlpatterns = [
path('',views.home,name = 'home'),
path('home.html',views.home2,name = 'home2'),
path('about.html',views.about,name = 'about'),
path('blog.html',views.blog,name = 'blog'),
path('blog_details.html',views.blog_details,name = 'blog_details'),
path('contact.html',views.contact,name = 'contact'),
path('pricing.html',views.pricing,name = 'pricing'),
path('service.html',views.service,name = 'service'),
]
