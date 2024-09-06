from typing import Any
from django.shortcuts import render, redirect, get_object_or_404
from . import models
from .forms import CustomForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.decorators import login_required
from django.views.generic import View, DetailView,CreateView,UpdateView,DeleteView
# Create your views here.

class PostCreateView(LoginRequiredMixin, CreateView):
    model = models.Post
    form = CustomForm
    fields = ('title', 'content', 'author','status', 'created_at')
    template_name = 'NewsApp/create.html'
    success_url = 'list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['title'] = 'create post'
        return context

class ListView(View):
    template_name = "NewsApp/list.html"

    def get(self, request):
        title = 'list'
        posts = models.Post.objects.all()
        paginator = Paginator(posts, 5, orphans=4, allow_empty_first_page=True)
        page = request.GET.get('page')
        try:
            posts_paginated = paginator.page(page)
        except PageNotAnInteger:
            posts_paginated = paginator.get_page(1)
        except EmptyPage:
            posts_paginated = paginator.get_page(paginator.num_pages)
        return render(request, self.template_name,{'posts': posts_paginated, 'title': title})

class PostDetailView(DetailView):
    model = models.Post
    template_name = 'NewsApp/detail.html'
    context_object_name = 'post'
    def get_context_data(self, **kwargs):
        context =super().get_context_data(**kwargs)
        context ['title'] = 'post detail'
        return context

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Post
    form = CustomForm
    fields = ('title', 'content', 'author','status', 'created_at')
    template_name = 'NewsApp/update.html'
    context_object_name = 'post'
    success_url ='list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'update post' 
        return context
        form = CustomForm(instance=post)
        title = 'update'
        return render(request, 'NewsApp/update.html', {'form': form, 'post': post, 'title':title})
    

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Post
    template_name = 'NewsApp/delete.html'
    context_object_name = 'post'
    success_url ='list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'delete post' 
        return context
