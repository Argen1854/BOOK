from django.urls import path
from . import views

urlpatterns = [
    path('book/', views.BookListView.as_view(), name="book"),
    path('book/<int:id>/', views.BookDetailView.as_view(), name='book_detail'),
    path('book/<int:id>/update/', views.UpdateBookView.as_view(), name='book_update'),
    path('book/<int:id>/delete/', views.DeleteBook.as_view(), name='book_delete'),
    path('book/create/', views.CreateBookView.as_view(), name='create_book')
]