from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
from django.views import generic
from django.shortcuts import redirect
from django.core.paginator import Paginator

from .models import Post

class IndexView(generic.ListView):
    template_name = 'blogi/index.html'
    context_object_name = 'latest_post_list'
    pages = 100

    def get_queryset(self):
        return Post.objects.filter(
            pub_date__lte=timezone.now()
            ).order_by('-pub_date')[:self.pages]


class DetailView(generic.DetailView):
    model = Post
    template_name = 'blogi/detail.html'

    def get_queryset(self):
        return Post.objects.filter(pub_date__lte=timezone.now())

class AddView(generic.ListView):
    model = Post
    template_name = 'blogi/add_numbers.html'

def add_numbers(request):
    if request.method == 'POST':
        try:
            number1 = request.POST['number1']
            number2 = request.POST['number2']
            result = int(number1) + int(number2)
            return render(request, 'blogi/add_numbers.html', {'number1': number1, 'number2':number2,'result': result})
        except:
            return render(request, 'blogi/add_numbers.html', {'number1': "error", 'number2':"error", 'result': "error"})
    else:
        return render(request, 'blogi/add_numbers.html')

def read(request, question_id):
    post = get_object_or_404(Post, pk=question_id)
    return render(request, 'blogi/detail.html')

def view_404(request, exception=None):
    return redirect('/blogi')