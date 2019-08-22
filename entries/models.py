from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from users.models import Profile
from django.urls import reverse

class Entry(models.Model):
    title = models.CharField(max_length= 30)
    text = models.TextField(max_length = 500)
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural= "entries"

    def get_absolute_url(self):
        return reverse('entry-detail', kwargs={'pk':self.pk})
