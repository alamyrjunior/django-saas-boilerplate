from django.http import HttpResponse
from django.shortcuts import render
from visits.models import PageVisit
def home_view(request, *args, **kwargs):
    total_visits = PageVisit.objects.count()
    visits = PageVisit.objects.filter(path=request.path)

    context = {
        'page_title': 'Home Page',
        'visits': visits.count(),
        'total_visits': total_visits,
    }
    PageVisit.objects.create(path=request.path)
    return render(request, 'home.html', context)

def about_view(request, *args, **kwargs):
    total_visits = PageVisit.objects.count()
    visits = PageVisit.objects.filter(path=request.path)

    context = {
        'page_title': 'Home Page',
        'visits': visits.count(),
        'total_visits': total_visits,
    }
    PageVisit.objects.create(path=request.path)
    return render(request, 'home.html', context)
