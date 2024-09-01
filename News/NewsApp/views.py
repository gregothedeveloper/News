from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from . import models
from .forms import CustomForm

# Create your views here.
def post_create(request,):
    if request.method == 'POST':
        form = CustomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = CustomForm()
    return render(request, 'NewsApp/create.html', {'form': form})
def post_list(request):
    posts = models.Post.objects.all()
    return render(request, 'NewsApp/list.html', {'posts': posts})

def post_detail(request, id):
    post = get_object_or_404(models.Post, id=id)
    return render(request, 'NewsApp/detail.html', {'post': post})

def post_update(request, id):
    post = get_object_or_404(models.Post, id=id)
    if request.method == 'POST':
        form = CustomForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('detail', id=post.id)
    else:
        form = CustomForm(instance=post)
        return render(request, 'NewsApp/update.html', {'form': form, 'post': post})
    
def post_delete(request, id):
    post = get_object_or_404(models.Post, id=id)
    if request.method == 'POST':
        post.delete()
        return redirect('list')
    return render(request, 'NewsApp/delete.html', {'post': post})
