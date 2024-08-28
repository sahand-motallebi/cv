from django.utils import timezone
from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(null=True)
    subject = models.TextField(default=True)
    message = models.TextField(default=True)
    published_date = models.DateTimeField(default=timezone.now)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_date']
        verbose_name = 'CONTACT FORM'
        verbose_name_plural = 'CONTACT FORMS'

    def __str__(self):
        return '{} - {}'.format(self.name, self.email)