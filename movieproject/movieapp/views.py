from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Movie
from .forms import mform

# Create your views here.

def index(request):
    movie=Movie.objects.all()
    context={
        'movie_list':movie
    }
    return render(request,'index.html',context)

def detail(request,movie_id):
    moovi=Movie.objects.get(id=movie_id)
    return render(request,"detail.html",{'movie':moovi})
def add_movie(request):
    if request.method=="POST":
        name1=request.POST.get('name',)
        desc1= request.POST.get('desc',)
        yr = request.POST.get('year',)
        img1=request.FILES['img']
        movie=Movie(name=name1,desc=desc1,year=yr,img=img1)
        movie.save()
    return render(request,'add.html')
def update(request,id):
    movie=Movie.objects.get(id=id)
    form=mform(request.POST or None,request.FILES,instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'movie':movie})

def delete(request,id):
    if request.method=="POST":
        movee=Movie.objects.get(id=id)
        movee.delete()
        return  redirect('/')
    return render(request,'delete.html')