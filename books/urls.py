from rest_framework import routers
from django.urls import path

from .views import BookViewSet, generate_books_view

router = routers.SimpleRouter()
router.register('books', BookViewSet, basename='books')

# router.register('books', BookDetailViewSet, basename='books')

urlpatterns = [
    path('generate-books/', generate_books_view, name='generate-books'),
    
]

urlpatterns += router.urls
