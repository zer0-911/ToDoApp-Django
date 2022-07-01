from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'todo/index.html')   

def done(request):
    return render(request, 'todo/index.html')   

def pending(request):
    return render(request, 'todo/index.html')   

def delete_all(request):
    return render(request, 'todo/index.html')    

def create(request):
    return render(request, 'todo/index.html')   

def update(request, id):
    return render(request, 'todo/index.html')  

def delete(request, id):
    return render(request, 'todo/index.html')   