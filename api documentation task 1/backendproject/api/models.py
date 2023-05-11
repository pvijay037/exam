from django.db import models
from django.contrib.auth.models import User
import uuid



class Event(models.Model):
    name = models.CharField(max_length=255)
    uid = models.UUIDField(default=uuid.uuid4, editable=False)
    tagline = models.CharField(max_length=255)
    schedule = models.DateTimeField()
    description = models.TextField()
    image = models.ImageField(upload_to='event_images')
    moderator = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=255)
    sub_category = models.CharField(max_length=255)
    rigor_rank = models.IntegerField()
    attendees = models.ManyToManyField(User, related_name='events_attending')

    def __str__(self):
        return self.name

