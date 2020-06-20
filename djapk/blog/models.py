from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    date_created = models.DateTimeField(default=timezone.now)
    post = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)


    def __repr__(self):
        return 'id : {0} title: {1} post :{2}'.format(self.id, self.title, self.post)


    def get_absolute_url(self):
        return reverse('each', kwargs={'pk': self.pk})
