from django.db import models
from organization.models import Organization


class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    organization = models.ManyToManyField(Organization, related_name='organizations')
    image = models.ImageField(upload_to='static/images/')
    date = models.DateTimeField()

    def __str__(self):
        return f"{self.title} - {self.date.strftime('%d.%m.%Y, %H:%M')}"

    class Meta:
        verbose_name = "Event"
        verbose_name_plural = "Events"
        ordering = ['pk', 'date']
