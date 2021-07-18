from elasticsearch_dsl import Q
from ..documents import AuthorDocument, BookDocument


class SearchService:

    def get_books(self, **kwargs):
        keyword = kwargs.get('keyword')
        query = Q("multi_match", query=keyword, fields=['title', 'isbn'])
        books = BookDocument.search().query(query)
        return books

    def get_authors(self, **kwargs):
        authors = AuthorDocument.search().query("match", description="beautiful")
        return authors
