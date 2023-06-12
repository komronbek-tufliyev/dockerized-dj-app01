from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField()
    publisher = models.CharField(max_length=255)
    publication_date = models.DateField()
    STATUS = (
        ('available', 'Available'),
        ('unavailable', 'Unavailable'),
    )
    thumbnail = models.ImageField(upload_to='thumbnails', null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    status = models.CharField(max_length=255, choices=STATUS, default='available')

    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'books'
        ordering = ['-created_at']

        