
from django.db.models.base import Model as Model
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
)

from .models import Article
from .forms import ArticleModelForm

# Create your views here.


class AritcleListView(ListView):
    # here we are overriding our template names. Cuz by default django wants
    # name something like like that  <blog>/<modelName>_list.html but we want to use our custom so:
    template_name = 'articles/article_list.html'
    queryset = Article.objects.all()
    # here I do not have to do render, do not have to write template name etc. Just because of django builtin
    # ListView. I have inherite Listview inside my ArticleListView class


class AritcleDetailView(DetailView):
    template_name = 'articles/article_detail.html'

    def get_object(self):
        # <-- This is how we grab id from the url in class based views
        id_ = self.kwargs.get("pk")
        return get_object_or_404(Article, id=id_)

# note: In class based views the class views are inherite from other classes therefore, we have to override the things
# like we have done above by using get_object()


class AritcleCreateView(CreateView):
    template_name = 'articles/article_create.html'
    form_class = ArticleModelForm
    queryset = Article.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class AritcleUpdateView(UpdateView):
    template_name = 'articles/article_create.html'
    form_class = ArticleModelForm
    queryset = Article.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(Article, id=id_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class AritcleDeleteView(DeleteView):
    template_name = 'articles/article_delete.html'

    def get_object(self):
        # <-- This is how we grab id from the url in class based views
        id_ = self.kwargs.get("pk")
        return get_object_or_404(Article, id=id_)
    def get_success_url(self) :
        return reverse('article-list')
