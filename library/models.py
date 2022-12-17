from django.db import models
from django.contrib.auth.models import User
from  django.conf.global_settings import AUTH_USER_MODEL


class Author(models.Model):
    name = models.CharField(max_length=500,help_text="Name of the author")

    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(max_length=500,help_text="Name of the publisher")

    def __str__(self):
        return self.name


class BookInstance(models.Model):
    book = models.ForeignKey("Book",on_delete=models.CASCADE)
    date_taken = models.DateField(auto_now=True)
    return_date = models.DateField()
    taken_by = models.ForeignKey(AUTH_USER_MODEL,on_delete=models.SET_NULL,null=True)

def __str__(self):
        return self.book


class Book(models.Model):
    BOOKS_LANGUAGES = [
        ("ENG","English"),
        ("FRE","French"),
        ("ARA","Arabic"),
        ("SWA","Swahili"),
    ]

    BOOK_TYPES = [
        ("REL","Religion"),
        ("NOV","Novel"),
        ("HIS","History"),
        ("TXB","Text Book"),

    ]

    title = models.CharField(max_length=500,help_text="Title of the book")
    book_cover=models.URLField()
    description = models.TextField(help_text='Brief description of the book')
    publication_date = models.DateField(help_text="Date this book was published")
    publisher= models.ForeignKey(Publisher,on_delete=models.SET_NULL,help_text="The publisher of the book",null=True)
    authors = models.ManyToManyField(Author,help_text="The authors of the book",related_name="books")
    type=models.CharField(max_length=3,choices=BOOK_TYPES,help_text="Book genre" )
    language=models.CharField(max_length=3,choices=BOOKS_LANGUAGES )
    copies = models.PositiveIntegerField(help_text="number of copies",default=1)
    
    def __str__(self):
        return f"{self.title[:60]} ..." if len(self.title) > 60 else self.title
    
