from django.contrib import admin
from django.urls import include, path
from home.views import HomeView  # Import the home view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", HomeView.as_view(), name='default_home'),  # Set the default URL to the home page
    path("auctions/", include("auctions.urls")),
    path("home/", include("home.urls")),
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
