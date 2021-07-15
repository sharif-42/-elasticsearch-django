from django.urls import path
from search import views


urlpatterns = [
    path('books/',  views.BookSearchAPIView.as_view(), name='book-search'),
]
