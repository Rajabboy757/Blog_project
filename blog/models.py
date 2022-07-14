import asyncio

from django.db import models

# Create your models here.
from django.dispatch import receiver
from django.urls import reverse
from django.db.models.signals import post_save

from blog.bot import sendd


class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE
    )

    body = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.pk)])

def form_sender(sender, instance, **kwargs):
    asyncio.run(sendd(instance.title, instance.body, instance.author))
    return True

post_save.connect(form_sender, sender=Post)