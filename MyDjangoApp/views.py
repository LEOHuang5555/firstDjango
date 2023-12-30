from django.shortcuts import render

# Create your views here.

def home(request):
    print(request)
    return render(request, 'MyDjangoApp/home.html')

