from django.db import models


class Hub(models.Model):
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    time_delta_check = models.DurationField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
