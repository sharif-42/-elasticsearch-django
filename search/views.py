from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView

from .services.search_services import SearchService
from .serializers import BookSearchSerializer


class BookSearchAPIView(ListAPIView):
    service_class = SearchService
    serializer_class = BookSearchSerializer

    def get(self, request, *args, **kwargs):
        query_params_dict = self.request.query_params.dict()
        books = self.service_class().get_books(**query_params_dict)
        serializer = self.serializer_class(instance=books, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
