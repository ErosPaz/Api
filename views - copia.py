from django.http import JsonResponse
from rest_framework import viewsets
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def filter_by_year(self, request):
        year = request.GET.get('year', None)
        if year is not None:
            books = Book.objects.filter(published_date__year=year)
        else:
            books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return JsonResponse(serializer.data, safe=False)
