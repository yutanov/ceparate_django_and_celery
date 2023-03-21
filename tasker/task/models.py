from django.db import models


class AsyncResults(models.Model):
    filename = models.CharField(max_length=120, blank=False, null=False)
    created_at = models.DateTimeField(auto_now=False)
    n_rows = models.IntegerField(null=True)
    finished_at = models.DateTimeField(auto_now=False, null=True)
    result = models.CharField(max_length=120, blank=False)
