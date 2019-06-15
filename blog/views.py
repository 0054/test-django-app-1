from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View

from .models import Post, Tag
from .utils import *
from .forms import TagForm, PostForm


def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', context={'posts': posts})

def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tags_list.html', context={'tags': tags})



class PostDetail(ObjectDetailMixin, View):
    template = 'blog/post_detail.html'
    model = Post

class PostUpdate(ObjectUpdateMixin, View):
    model = Post
    form_model = PostForm
    template = 'blog/post_update.html'

class PostCreate(ObjectCreateMixin, View):
    form_model = PostForm
    template = 'blog/post_create.html' 

class TagDetail(ObjectDetailMixin, View):
    template = 'blog/tag_detail.html'
    model = Tag

class PostDelete(ObjectDeleteMixin, View):
    model = Post
    template = 'blog/post_delete.html'
    redirect_template = 'posts_list_url'

class TagDelete(ObjectDeleteMixin, View):
    model = Tag
    template = 'blog/tag_delete.html'
    redirect_template = 'tags_list_url'


class TagCreate(ObjectCreateMixin, View):
    form_model = TagForm
    template = 'blog/tag_create.html'

class TagUpdate(ObjectUpdateMixin, View):
    model = Tag
    form_model = TagForm
    template = 'blog/tag_update.html'
