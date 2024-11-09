from .views import home_page_view
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page_view, name='home'),
]
