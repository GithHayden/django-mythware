from django.db import models
from django.utils import timezone


class Post(models.Model):
    """
    A single issue that is posted by a user.
    """
    title = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True,
                                          default=timezone.now)
    author = models.CharField(max_length=30, blank=True, null=True)
    issue_type = models.CharField(max_length=30, blank=True, null=True)
    amount_paid = models.CharField(max_length=30, blank=True, null=True)
    status = models.CharField(max_length=30, blank=True, null=True)
    details = models.TextField()

    def __unicode__(self):
        return self.title