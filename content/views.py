from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
from django.shortcuts import render_to_response, render
from django.template import RequestContext
from content.forms import BlogForm
from content.models import BlogContent


@permission_required('content.post_list', login_url='/admin/login/')
def post_list(request):
    context = {'posts': BlogContent.objects.all().order_by('-created'),
               'all_users': User.objects.all()}
    return render(request, 'index.html', context)

'''

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

    form = BlogForm(request.POST or None)

    if form.is_valid():
        save = form.save(commit=False)
        save.save()

    return render_to_response("form.html", locals(),
                              context_instance=RequestContext(request))