from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views
from .views import *

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),

    path("create", views.create, name="create"),
    path("insert", views.insert, name="insert"),
    path("listing/<int:id>", views.listing, name="listing"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("watch/<int:id>", views.watch, name="watch"),
    path("unwatch/<int:id>", views.unwatch, name="unwatch"),
    path("categories", views.categories, name="categories"),
    path("filter", views.filter, name="filter"),
    path('user', views.user_profile, name='user_profile'),

    path("update-bid/<int:id>", views.update_bid, name="update_bid"),
    path("close-bid/<int:id>", views.close_bid, name="close_bid"),

    path("comments/<int:id>", views.add_comment, name="add_comment"),
    path('delete_account', views.delete_account, name='delete_account'),
    path('avatar_update', views.update_avatar, name='update_avatar'),
    path('update_user_details', update_user_details, name='update_user_details'),
    path('update_user_password/', update_user_password, name='update_user_password'),
    path('payment/', payment_page, name='payment_page'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
