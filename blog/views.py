from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View

from .models import Post, Tag
from .utils import ObjectDetailMixin, ObjectCreateMixin
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

class TagDetail(ObjectDetailMixin, View):
    template = 'blog/tag_detail.html'
    model = Tag


# class PostCreate(View):
#     def get(self, request):
#         form = PostForm()
#         return render(request, 'blog/post_create.html', context={'form': form})

#     def post(self, request):
#         bound_form = PostForm(request.POST)
#         if bound_form.is_valid():
#             new_post = bound_form.save()
#             return redirect(new_post)
#         return render(request, 'blog/post_create_form.html', context={'form': bound_form})

class PostCreate(ObjectCreateMixin, View):
    form_model = PostForm
    template = 'blog/post_create.html' 

class TagCreate(ObjectCreateMixin, View):
    form_model = TagForm
    template = 'blog/tag_create.html'

# class TagCreate(View):

#     def get(self, request):
#         form = TagForm()
#         return render(request, 'blog/tag_create.html', context={'form': form})

#     def post(self, request):
#         bound_form = TagForm(request.POST)
#         if bound_form.is_valid():
#             new_tag = bound_form.save()
#             return redirect(new_tag)
#         return render(request, 'blog/tag_create.html', context={'form': bound_form})

    

