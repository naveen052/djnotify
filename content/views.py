from django.shortcuts import render_to_response

from django.template import RequestContext

from content.forms import BlogForm

from content.models import BlogContent


def post_list(request):
    posts = BlogContent.objects.all()
    return render_to_response("index.html", {"posts": posts})

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


def add_content(request):

    form = BlogForm(request.POST or None)

    if form.is_valid():
        save = form.save(commit=False)
        save.save()

    return render_to_response("form.html", locals(),
                              context_instance=RequestContext(request))