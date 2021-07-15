from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry

from library.models import Author, Book


@registry.register_document
class AuthorDocument(Document):
    pk = fields.IntegerField()

    class Index:
        # Name of the Elasticsearch index
        name = 'authors'
        # See Elasticsearch Indices API reference for available settings
        settings = {'number_of_shards': 1,
                    'number_of_replicas': 0}

    class Django:
        model = Author  # The model associated with this Document

        # The fields of the model you want to be indexed in Elasticsearch
        fields = [
            'first_name',
            'last_name',
            'author_name',
            'email',
        ]

        # Ignore auto updating of Elasticsearch when a model is saved
        # or deleted:
        # ignore_signals = True

        # Don't perform an index refresh after every update (overrides global setting):
        # auto_refresh = False

        # Paginate the django queryset used to populate the index with the specified size
        # (by default it uses the database driver's default setting)
        # queryset_pagination = 5000


@registry.register_document
class BookDocument(Document):
    author = fields.ObjectField(properties={
        'pk': fields.IntegerField(),
        'first_name': fields.KeywordField(),
        'last_name': fields.KeywordField(),
        'author_name': fields.KeywordField(),
        'email': fields.TextField(),
    })

    pk = fields.IntegerField()
    isbn = fields.KeywordField()

    class Index:
        # Name of the Elasticsearch index
        name = 'books'
        # See Elasticsearch Indices API reference for available settings
        settings = {'number_of_shards': 1,
                    'number_of_replicas': 0}

    class Django:
        model = Book  # The model associated with this Document

        # The fields of the model you want to be indexed in Elasticsearch
        fields = [
            'title',
            'publishing_date',
        ]
        related_models = [Author]

    def get_instances_from_related(self, related_instance):
        """If related_models is set, define how to retrieve the Book instance(s) from the related model."""
        if isinstance(related_instance, Author):
            return related_instance.books.all()
