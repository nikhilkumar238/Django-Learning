
from django.urls import path
from .views import (
    dynamic_lookup_view, 
    article_list_view, 
    ArticleListView, 
    ArticleDetailView,
    ArticleCreateView,
    ArticleUpdateView,
    ArticleDeleteView
    )

app_name="blog"
urlpatterns = [
    path('', ArticleListView.as_view(), name="article-list"),
    path('article_details/<int:id>/', ArticleDetailView.as_view(), name="article-detail"),
    path('create/', ArticleCreateView.as_view(), name="article-create"),
    path('<int:id>/update/', ArticleUpdateView.as_view(), name="article-update"),
    path('<int:id>/delete/', ArticleDeleteView.as_view(), name="article-delete"),
    # path('', article_list_view, name="blog"), 
    # path('article_details/<int:id>/', dynamic_lookup_view, name="article_search"),    
]