from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Organization(models.Model):
    title = models.CharField(max_length=255, verbose_name='title', unique=True)
    description = models.TextField()
    address = models.CharField(max_length=255, verbose_name='address')
    postcode = models.CharField(max_length=50, verbose_name='postcode')

    def __str__(self):
        return f"{self.title} - {self.address} - {self.postcode}"

    class Meta:
        verbose_name = "Organization"
        verbose_name_plural = "Organizations"
        ordering = ['pk', 'title', 'postcode']
