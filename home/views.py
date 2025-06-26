from django.http import HttpResponse

def home(request):
    return HttpResponse("This is my dev application")
