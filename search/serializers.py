from rest_framework import serializers

from library.models import Book


class BookSearchSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = [
            'pk', 'title', 'author', 'isbn', 'publishing_date',
        ]

    def get_author(self, instance):
        return instance.author.author_name
