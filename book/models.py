from operator import truth
from django.db import models

# Create your models here.
class BookList(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="")
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __sts__(self):
        return self.title

class BookComment(models.Model):
    shows = models.ForeignKey(BookList, on_delete=models.CASCADE, related_name="book_commet")
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.shows.title
    
class Expert(models.Model):
    EXPERT_ACTIVITY = [
        ('reader', 'reader'),
        ('manga', 'manga'),
        ('writer', 'writer')
    ]
    name = models.CharField(max_length=100)
    activity = models.CharField(max_length=100, choices=EXPERT_ACTIVITY)
    information = models.TextField()

class ExpertRecomendation(models.Model):
    book = models.ForeignKey(BookList, on_delete=models.CASCADE, related_name='expert_rec')
    review = models.TextField()
    expert = models.ForeignKey(Expert, on_delete=models.CASCADE, related_name='expert_book')