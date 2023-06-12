# tasks.py

from celery import shared_task
from datetime import date
from faker import Faker
import random

from .models import Book

fake = Faker()

statuses = ['available', 'unavailable']

@shared_task
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
