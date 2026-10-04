from django.db import models

choise_of_janr = (
    ('badiiy', 'Badiiy'),
    ('ilmiy', 'Ilmiy'),
    ('horror', 'Horror'),
    ('romance', 'Romance'),
    ('detective', 'Detective')
)

class Book(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits = 10, decimal_places= 2)
    quantity = models.PositiveBigIntegerField(default= 1)
    author = models.CharField(max_length=200, null=True, blank=True)  
    type_janr = models.CharField(max_length=200, choices=choise_of_janr)  
    def __str__(self):
        return f'{self.name}-{self.author}-{self.price}'
    class Meta:
        verbose_name = 'book'
        verbose_name_plural = 'books'
        ordering = ['-name']