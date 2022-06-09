from django.urls import reverse_lazy
from django.shortcuts import render
from datetime import datetime
from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView)
from .models import Post
from .filters import PostFilter
from .forms import PostForm, NewsForm, ArticleForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import TemplateView

# class Author(PermissionRequiredMixin, View):
#     permission_required = ('news.view_Post',
#                            'news.add_Post',
#                            'news.change_Post')

class PostList(ListView):
    model = Post
    ordering = ['-dateCreation']
    template_name = 'posts.html'
    context_object_name = 'Post'
    paginate_by = 10  # вот так мы можем указать количество записей на странице

class PostDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Post
    template_name = 'post.html'
    permission_required = ('news.view_Post',
                           'news.add_Post',
                           'news.change_Post'
                           )
    # Название объекта, в котором будет выбранный пользователем продукт
    context_object_name = 'post-one'


class NewsCreate(CreateView):
    form_class = NewsForm
    model = Post
    template_name = 'news_create.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.categoryType = 'NW'
        return super().form_valid(form)

def create_news():
    form = NewsForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/posts/')

    return render(request, 'news_create.html', {'form': form})

class NewsEdit(UpdateView):
    form_class = NewsForm
    model = Post
    template_name = 'news_edit.html'


class NewsDelete(DeleteView):
    model = Post
    template_name = 'news_delete.html'
    success_url = reverse_lazy('post_list')

class ArticleCreate(CreateView):
    form_class = ArticleForm
    model = Post
    template_name = 'article_create.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.categoryType = 'AR'
        return super().form_valid(form)

def create_article():
    form = ArticleForm()
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/posts/')

    return render(request, 'article_create.html', {'form': form})

class ArticleEdit(UpdateView):
    form_class = ArticleForm
    model = Post
    template_name = 'article_edit.html'


class ArticleDelete(DeleteView):
    model = Post
    template_name = 'article_delete.html'
    success_url = reverse_lazy('post_list')


class NewsSearch:
    model = Post
    ordering = 'title'
    template_name = 'posts.html'
    context_object_name = 'posts'
    paginate_by = 10
    def get_queryset(self):
        queryset = super().get_queryset()
        # Используем наш класс фильтрации.
        # self.request.GET содержит объект QueryDict, который мы рассматривали
        # в этом юните ранее.
        # Сохраняем нашу фильтрацию в объекте класса,
        # чтобы потом добавить в контекст и использовать в шаблоне.
        self.filterset = PostFilter(self.request.GET, queryset)
        # Возвращаем из функции отфильтрованный список товаров
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Добавляем в контекст объект фильтрации.
        context['filterset'] = self.filterset
        return context


