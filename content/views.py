from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

from django.views.generic import View

from content.forms import BlogForm, PostTypeVideoForm

from content.models import BlogContent, PostTypeVideo


# ----------------------------Normal Post---------------------------------------------------


class PostList(View):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        context = {
            "posts": BlogContent.objects.all().order_by('-created')
        }
        return render(request, self.template_name, context)


def add_content(request):

    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES)
        form.save()
        return HttpResponseRedirect('/')
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
            post.save()
            return redirect('content.views.PostList', pk=post.pk)
    else:
        form = BlogForm(instance=post)
    return render(request, 'edit.html', {'form': form})


# ----------------------Video Post---------------------------------------------------------


def add_post_type_video(request):
    if request.method == "POST":
        video_form = PostTypeVideoForm(request.POST, request.FILES)
        video_form.save()
        return HttpResponseRedirect('/')
    else:
        video_form = PostTypeVideoForm()
    return render(request, 'video_form.html', {'form': video_form})


class VideoTypePostList(View):
    template_name = 'video.html'

    def get(self, request, *args, **kwargs):
        context = {
            "posts": PostTypeVideo.objects.all()
        }
        return render(request, self.template_name, context)


def delete_video_post(request, pk):
    post = get_object_or_404(PostTypeVideo, pk=pk)
    post.delete()
    return redirect('/', pk=post.pk)


def edit_video_post(request, pk):
    post = get_object_or_404(PostTypeVideo, pk=pk)
    if request.method == "POST":
        form = PostTypeVideoForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('/video', pk=post.pk)
    else:
        form = PostTypeVideoForm(instance=post)
    return render(request, 'edit_video.html', {'form': form})

