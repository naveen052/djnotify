from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect, render_to_response

from django.views.generic import View

from content.forms import BlogForm, PostTypeVideoForm, PostTypeAudioForm, AddCategoryForm

from content.models import BlogContent, PostTypeVideo, PostTypeAudio, Category


# ----------------------------Normal Post---------------------------------------------------


class PostList(View):
    template_name = 'index.html'

    def get(self, request):
        context = {
            "posts": BlogContent.objects.all().order_by('-created'),
            "title": "Latest Posts"
        }
        return render(request, self.template_name, context)


def add_content(request):

    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            return HttpResponseRedirect('/')
        else:
            form = BlogForm()
    else:
        form = BlogForm()
    return render(request, 'form.html', {'form': form, 'title': "Add Post"})


def add_category(request):

    if request.method == "POST":
        form = AddCategoryForm(request.POST, request.FILES)
        form.save()
        return HttpResponseRedirect('/')
    else:
        form = AddCategoryForm()
    return render(request, 'category.html', {'form': form, 'title': "Add Category"})


def view_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return render_to_response('view_category.html', {
        'category': category,
        'title': "Viewing post for category",
        'posts': BlogContent.objects.filter(category=category)[:5]
    })


def delete_post(request, pk):
    post = get_object_or_404(BlogContent, pk=pk)
    post.delete()
    return redirect('/', pk=post.pk)


def view_post(request, pk):
    return render_to_response('single_post.html', {
        'post': get_object_or_404(BlogContent, pk=pk)
    })


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
    return render(request, 'edit.html', {'form': form, 'title': "Edit Post"})


# ----------------------Video Post---------------------------------------------------------


def add_post_type_video(request):
    if request.method == "POST":
        video_form = PostTypeVideoForm(request.POST, request.FILES)
        video_form.save()
        return HttpResponseRedirect('/')
    else:
        video_form = PostTypeVideoForm()
    return render(request, 'video_form.html', {'form': video_form, 'title': "Add Video Post"})


class VideoTypePostList(View):
    template_name = 'video.html'

    def get(self, request, *args, **kwargs):
        context = {
            "posts": PostTypeVideo.objects.all(),
            "title": "Your Videos"
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
    return render(request, 'edit_video.html', {'form': form, 'title': "Edit Video post"})


# ----------------------Video Post---------------------------------------------------------


def add_post_type_audio(request):
    if request.method == "POST":
        audio_form = PostTypeAudioForm(request.POST, request.FILES)
        audio_form.save()
        return HttpResponseRedirect('/')
    else:
        audio_form = PostTypeAudioForm()
    return render(request, 'audio_form.html', {'form': audio_form, 'title': "Add Audio Post"})


class AudioTypePostList(View):
    template_name = 'audio.html'

    def get(self, request, *args, **kwargs):
        context = {
            "posts": PostTypeAudio.objects.all(),
            "title": "Your Audio Clips"
        }
        return render(request, self.template_name, context)


def delete_audio_post(request, pk):
    post = get_object_or_404(PostTypeAudio, pk=pk)
    post.delete()
    return redirect('/', pk=post.pk)


def edit_audio_post(request, pk):
    post = get_object_or_404(PostTypeAudio, pk=pk)
    if request.method == "POST":
        form = PostTypeAudioForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('/video', pk=post.pk)
    else:
        form = PostTypeVideoForm(instance=post)
    return render(request, 'edit_audio.html', {'form': form, 'title': "Edit Audio post"})

