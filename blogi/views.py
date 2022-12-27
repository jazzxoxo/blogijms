from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
from django.views import generic
from django.shortcuts import redirect

from .models import Post


class IndexView(generic.ListView):
    template_name = 'blogi/index.html'
    context_object_name = 'latest_post_list'

    def get_queryset(self):
        return Post.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Post
    template_name = 'blogi/detail.html'

    def get_queryset(self):
        return Post.objects.filter(pub_date__lte=timezone.now())


def read(request, question_id):
    post = get_object_or_404(Post, pk=question_id)
    return render(request, 'blogi/detail.html')

def view_404(request, exception=None):
    return redirect('/blogi')