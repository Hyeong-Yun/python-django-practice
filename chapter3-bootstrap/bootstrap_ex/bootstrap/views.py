from django.shortcuts import render

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def youtube(requset):
  return render(requset, 'youtube.html')

def son(request):
  return render(request, 'son.html')

def wpt(request):
  return render(request, 'WPT.html')