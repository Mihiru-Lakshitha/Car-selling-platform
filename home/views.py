from django.shortcuts import render
from django.views import View

class HomeView(View):
    def get(self, request):
        return render(request, 'home/home.html')

class ServiceView(View):
    def get(self, request):
        return render(request, 'home/service.html')

class TeamView(View):
    def get(self, request):
        return render(request, 'home/team.html')

class TestimonialView(View):
    def get(self, request):
        return render(request, 'home/testimonial.html')

class PageNotFoundView(View):
    def get(self, request):
        return render(request, 'home/404.html')

class AboutView(View):
    def get(self, request):
        return render(request, 'home/about.html')

class BookingView(View):
    def get(self, request):
        return render(request, 'home/booking.html')

class ContactView(View):
    def get(self, request):
        return render(request, 'home/contact.html')

class ForumView(View):
    def get(self, request):
        return render(request, 'home/forum.html')
class BlogView(View):
    def get(self, request):
        return render(request, 'home/blog.html')
