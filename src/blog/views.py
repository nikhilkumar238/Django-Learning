from django.shortcuts import render, get_object_or_404, redirect
from .models import Article
# from .forms import ProductFrom, RawProductForm
from django.http import Http404
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
)
from .forms import ArticleForm
from django.urls import reverse
# Create your views here.

class ArticleListView(ListView):
    template_name = 'article/article_list.html'
    queryset = Article.objects.all() #default it will look <blog>/<modelname>_list.html

class ArticleDetailView(DetailView):
    template_name = 'article/article_details.html'
    # queryset = Article.objects.all() #default it will look <blog>/<modelname>_list.html

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)
    
class ArticleCreateView(CreateView):
    template_name = 'article/article_create.html'
    form_class = ArticleForm
    # form_class = Articl
    queryset = Article.objects.all()
    # success_url = "/"
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

    # def get_success_url(self, form):
    #     return "/"

class ArticleUpdateView(UpdateView):
    template_name = 'article/article_create.html'
    form_class = ArticleForm
    # form_class = Articl
    queryset = Article.objects.all()
    # success_url = "/"
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)

    # def get_success_url(self, form):
    #     return "/"

class ArticleDeleteView(DeleteView):
    template_name = 'article/article_delete.html'
    # form_class = ArticleForm
    # form_class = Articl
    # queryset = Article.objects.all()
    # success_url = "/"
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)

    def get_success_url(self):
        return reverse('blog:article-list')

def article_list_view(request):
    queryset = Article.objects.all()
    context = {
        'obj': queryset
    }
    return render(request, "article/article_list.html", context)



def dynamic_lookup_view(request, id):
    # obj = Product.objects.get(id=id)
    # obj = get_object_or_404(Product, id=id)
    try:
        obj = Article.objects.get(id=id)
    except Product.DoesNotExist:
        raise Http404
    context = {
        "obj": obj
    }
    print(obj.title)
    return render(request, "article/article_details.html", context)

