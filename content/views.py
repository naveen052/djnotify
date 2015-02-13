from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View

from content.forms import BlogForm
from content.models import BlogContent


class PostList(View):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        context = {
            "posts": BlogContent.objects.all().order_by('-created')
        }
        return render(request, self.template_name, context)



@permission_required('/', login_url='/admin/login/')
def add_content(request):

    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('blog.views.PostList', pk=post.pk)
    else:
        form = BlogForm()
    return render(request, 'form.html', {'form': form})


def delete_post(request, pk):
    post = get_object_or_404(BlogContent, pk=pk)
    post.delete()
    return redirect('/', pk=post.pk)


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