from django.http import HttpResponse

def index(request):
    return HttpResponse('Главная страница')

def group_posts(request, slug):
    return HttpResponse(f'Посты в группе{slug}')

def name(request):
    return HttpResponse('Привет мидвед')

