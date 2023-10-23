from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100, default='Unknown')
    release_date = models.DateField()

    class Meta:
        unique_together = [['name', 'author', 'publisher', 'release_date']]

        def __str__(self) -> str:
            return f'{self.name}, {self.author} - Publisher: {self.publisher} ({self.release_date})'
