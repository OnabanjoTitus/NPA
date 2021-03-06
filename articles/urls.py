from django.urls import path

from articles.views import ArticleListView, ArticleUpdateView, ArticleDetailView, ArticleDeleteView, ArticleCommentView, \
    ArticleCreateView, \
    ArticleAboutView

urlpatterns = [
    path('<int:pk>/edit/',
         ArticleUpdateView.as_view(), name='article_edit'),
    path('<int:pk>/',
         ArticleDetailView.as_view(), name='article_detail'),
    path('<int:pk>/delete/',
         ArticleDeleteView.as_view(), name='article_delete'),
    path('', ArticleListView.as_view(), name='article_list'),
    path('new/', ArticleCreateView.as_view(), name='article_new'),
    path('about/', ArticleAboutView, name='about'),
    path('<int:pk>/comment/', ArticleCommentView.as_view(), name='article_comment'),
]
