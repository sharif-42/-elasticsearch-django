from ..documents import AuthorDocument, BookDocument


class SearchService:

    def get_books(self, **kwargs):
        books = BookDocument.search().query("match", title="never")
        return books

    def get_authors(self, **kwargs):
        authors = AuthorDocument.search().query("match", description="beautiful")
        return authors
