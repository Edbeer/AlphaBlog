from django.db.models import F
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.contrib import messages
from .models import *
from .forms import *


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully')
            return redirect('login')
        else:
            messages.error(request, 'Error')
    else:
        form = UserRegisterForm()
    return render(request, 'blog/register.html', {"form": form})


def login(request):
    return render(request, 'blog/login.html')


class Home(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    paginate_by = 4

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'DevBlog'
        return context


class GetPost(DetailView):
    model = Post
    template_name = 'blog/post.html'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        self.object.views = F('views') + 1
        self.object.save()
        self.object.refresh_from_db()
        return context


def add_post(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            Post.objects.create(**form.cleaned_data)
            return redirect('home')
    else:
        form = BlogForm()
    return render(request, 'blog/add_post.html', {'form': form})
