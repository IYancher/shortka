from django.db import models


class Shorturl(models.Model):
    user_url = models.CharField(max_length = 256)
    short_url = models.CharField(max_length = 256)
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True) 