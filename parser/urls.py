from django.urls import path
from . import views

urlpatterns = [
    path('parser/', views.ParserFormView.as_view(), name="parser"),
    path('parserlist/', views.ParserList.as_view(), name='parserlist'),
    path('parserlist/manga', views.ParserListManga.as_view(), name='parserlistmanga')
]