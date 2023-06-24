from django.http import HttpResponse
from rest_framework import views, status, viewsets
from rest_framework.response import Response
from .models import Book
from .tasks import generate_books
from rest_framework.decorators import action
from .serializers import BookSerializer
from rest_framework import permissions
from rest_framework.pagination import PageNumberPagination

class BookPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 1000

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = BookPagination


    @action(detail=False, methods=['post'])
    def generate_random_books(self, request):
        num_books = 10  # The number of books to generate
        generate_books(num_books)  # Call the task asynchronously
        return Response(status=status.HTTP_202_ACCEPTED)
    
def list_of_users(request):
    from django.contrib.auth.models import User
    users = User.objects.all()
    return HttpResponse(users)

def index(request):
    return HttpResponse('Hello, world. You\'re at the books index.')

from faker import Faker
import random

fake = Faker()

statuses = ['available', 'unavailable']

def generate_books(num_books):
    books = []
    for _ in range(num_books):
        title = fake.sentence(nb_words=3)
        author = fake.name()
        description = fake.paragraph(nb_sentences=3)
        publisher = fake.company()
        publication_date = fake.date_between(start_date='-10y', end_date='today')
        thumbnail = None
        status = random.choice(statuses)

        book = Book(
            title=title,
            author=author,
            description=description,
            publisher=publisher,
            publication_date=publication_date,
            thumbnail=thumbnail,
            status=status
        )
        books.append(book)

    Book.objects.bulk_create(books)


def generate_books_view(request):
    num_books = 10  # The number of books to generate
    generate_books(num_books)  # Call the task asynchronously
    return HttpResponse('Generating random books...')