from django.urls import path
from .views import HomeView, ServiceView, TeamView, TestimonialView, PageNotFoundView, AboutView, BookingView, ContactView, ForumView,BlogView

urlpatterns = [
    path("", HomeView.as_view(), name="default_home"),
    path("service/", ServiceView.as_view(), name="service"),
    path("team/", TeamView.as_view(), name="team"),
    path("testimonial/", TestimonialView.as_view(), name="testimonial"),
    path("404/", PageNotFoundView.as_view(), name="404"),
    path("about/", AboutView.as_view(), name="about"),
    path("booking/", BookingView.as_view(), name="booking"),
    path("contact/", ContactView.as_view(), name="contact"),
    path("forum/", ForumView.as_view(), name="forum"),
    path("blog/", BlogView.as_view(), name="blog"),
]

