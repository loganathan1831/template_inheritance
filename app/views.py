from django.shortcuts import render

# Create your views here.
def parant(request):
    return render(request,'parant.html')
def child(request):
    return render(request,'child.html')