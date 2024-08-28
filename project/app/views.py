from django.shortcuts import render

# Create your views here.

def indexfunc(request):
    return render(request, 'index.html')