Elasticsearch for Django
========================

This is a lightweight Django app for people who are using Elasticsearch with Django, and want to manage their indexes.

**NB the master branch is now based on ElasticSearch 7 and python**

----

Search Index Lifecycle
----------------------

The basic lifecycle for a search index is simple:

1. Create an index
2. Post documents to the index
3. Query the index

Relating this to our use of search within a Django project it looks like this:

1. Create mapping file for a named index
2. Add index configuration to Django settings
3. Map models to document types in the index
4. Post document representation of objects to the index
5. Update the index when an object is updated
6. Remove the document when an object is deleted
7. Query the index
8. Convert search results into a QuerySet (preserving relevance)

----

Re-Index elastic Search
-
```shell
python manage.py  search_index --rebuild -f
```