from .views import home_view, about_view
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path("about/", about_view, name='about')
]
