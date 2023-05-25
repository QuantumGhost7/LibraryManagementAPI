from django.urls import path
from LibraryApp.views import (
    get_all_books,
    get_book,
    create_book,
    update_book,
    delete_book,
)

urlpatterns = [
    path('books/', get_all_books),
    path('books/<str:book_id>/', get_book),
    path('books/create/', create_book),
    path('books/<str:book_id>/update/', update_book),
    path('books/<str:book_id>/delete/', delete_book),
]
