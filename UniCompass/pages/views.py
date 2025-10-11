from django.shortcuts import render, redirect
from django.utils import translation
from django.conf import settings

def set_language(request):
    if request.method == 'POST':
        language = request.POST.get('language')
        if language:
            translation.activate(language)
            response = redirect(request.META.get('HTTP_REFERER', 'home'))
            response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language)
            return response
    return redirect('home')

def home(request):
    return render(request, 'pages/home.html')

def calendar(request):
    return render(request, 'pages/calendar.html')

def tasks(request):
    return render(request, 'pages/tasks.html')

def knowledge_base(request):
    return render(request, 'pages/knowledge_base.html')

def contacts(request):
    return render(request, 'pages/contacts.html')

def mfc_detail(request):
    return render(request, 'pages/mfc_detail.html')