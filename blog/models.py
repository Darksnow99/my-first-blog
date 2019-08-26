from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200) # Textfeld mit max 200 Zeichen
    text = models.TextField() # Textfeld ohne Beschränkung
    created_date = models.DateTimeField(default=timezone.now) # Datum & Uhrzeit
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
