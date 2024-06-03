from django.db import models
from django.urls import reverse


# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=100, blank=False)
    descript = models.TextField()
    task_created_date = models.DateTimeField()
    deadline = models.DateTimeField()

    class Meta:
        verbose_name_plural="Ishlar"

    def __str__(self):
        return self.title

    def get_time_diff(self):
        return self.deadline - self.task_created_date <= 0

    def get_absolute_url(self):
        return reverse("task_detail", args=[self.pk])