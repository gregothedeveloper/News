from django.shortcuts import render, redirect, get_object_or_404
from . import models
from .forms import CustomForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def post_create(request,):
    if request.method == 'POST':
        form = CustomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = CustomForm()
        # title = 'create'
    return render(request, 'NewsApp/create.html', {'form': form})
def post_list(request):
    title = 'list'
    posts = models.Post.objects.all()
    paginator = Paginator(posts, 5, orphans=4, allow_empty_first_page=True)
    page = request.GET.get('page')
    try:
        posts_paginated = paginator.page(page)
    except PageNotAnInteger:
        posts_paginated = paginator.get_page(1)
    except EmptyPage:
        posts_paginated = paginator.get_page(Paginator.num_pages)
    return render(request, 'NewsApp/list.html',{'posts': posts_paginated, 'title': title})

def post_detail(request, id):
    title = 'detail'
    post = get_object_or_404(models.Post, id=id)
    return render(request, 'NewsApp/detail.html', {'post': post, 'title': title})

@login_required
def post_update(request, id):
    
    post = get_object_or_404(models.Post, id=id)
    if request.method == 'POST':
        form = CustomForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('detail', id=post.id)
    else:
        form = CustomForm(instance=post)
        title = 'update'
        return render(request, 'NewsApp/update.html', {'form': form, 'post': post, 'title':title})
    
@login_required
def post_delete(request, id):
    post = get_object_or_404(models.Post, id=id)
    if request.method == 'POST':
        post.delete()
        return redirect('list')
    title = 'delete'
    return render(request, 'NewsApp/delete.html', {'post': post, 'title': title})
