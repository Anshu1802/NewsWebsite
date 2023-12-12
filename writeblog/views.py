from django.shortcuts import render,redirect
from writeblog.models import CreateBlog
import requests

def home(request):
    homedata=CreateBlog.objects.all()
    context={'ansh':homedata}
    return render(request,"index.html",context)


def form(request):
    if request.method=='POST':
        data=request.POST
        blogimage=request.FILES.get('blogimage')
        title=data.get('title')
        description=data.get('description')
        link=data.get('link')
        CreateBlog.objects.create(blogimage=blogimage,title=title,description=description,link=link)
        return redirect('/')

    return render(request,"form.html")


def detail(request):
    api_url = 'https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=b0e82ec79db24a40ad76391a414b9cca'
    response = requests.get(api_url).json()
    context = {'response': response}
    return render(request, "detail.html", context)

def detail2(request):
    api_url = 'https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=b0e82ec79db24a40ad76391a414b9cca'
    response2 = requests.get(api_url).json()
    context2 = {'response2': response2}
    return render(request, "detail2.html", context2)

def detail3(request):
    api_url = 'https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=b0e82ec79db24a40ad76391a414b9cca'
    response3 = requests.get(api_url).json()
    context3 = {'response3': response3}
    return render(request, "detail3.html", context3)


def delete(request,id):
    queryset=CreateBlog.objects.get(id=id)
    queryset.delete()
    return redirect('/')
