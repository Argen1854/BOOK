from django.urls import path
from . import views

urlpatterns = [
    path('parser/', views.ParserFormView.as_view(), name="parser"),
    path('parser/list/anime', views.ParserList.as_view(), name='parserlist'),
    path('parser/list/manga', views.ParserListManga.as_view(), name='parserlistmanga'),
    path('parser/list/manga/<int:id>', views.MangaDetailView.as_view(), name="manga_d")
]