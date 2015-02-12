from django.contrib.auth.decorators import permission_required, login_required
from django.contrib.auth.models import User
from django.db.models.signals import post_syncdb
from django.shortcuts import render_to_response, render, redirect, get_object_or_404
from django.template import RequestContext
from django.utils.decorators import method_decorator
from django.views.generic import View

from content.forms import BlogForm
from content.models import BlogContent


class PostList(View):
    template_name = 'index.html'

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        context = {
            "posts": BlogContent.objects.all().order_by('-created'),
            "all_users": User.objects.all()
        }
        return render(request, self.template_name, context)

    post_syncdb.connect(get)

'''
def post_list(self):
        context = {'posts': BlogContent.objects.all().order_by('-created'),
                   'all_users': User.objects.all()}
        return render(request, 'index.html', context)
def post_list(request, year):
    posts = BlogContent.objects.values(created__year=year)

    context = {'article_list': posts, 'title': "Post list", "year":year}
    print posts
    return render(request, 'index.html', context)


def index(request):
    posts = BlogContent.objects.all().order_by("-created")

    return HttpResponse('This page shows a list of most recent posts.')
'''


@permission_required('content.post_list', login_url='/admin/login/')
def add_content(request):

    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('blog.views.PostList', pk=post.pk)
    else:
        form = BlogForm()
    return render(request, 'form.html', {'form': form})


def edit_post(request, pk):
    post = get_object_or_404(BlogContent, pk=pk)
    if request.method == "POST":
        form = BlogForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('content.views.PostList', pk=post.pk)
    else:
        form = BlogForm(instance=post)
    return render(request, 'edit.html', {'form': form})