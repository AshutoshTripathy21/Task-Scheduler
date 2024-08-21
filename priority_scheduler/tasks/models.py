# models.py
from django.db import models
from datetime import datetime, timedelta
from django.utils import timezone

class Task(models.Model):
    PRIORITY_CHOICES = [
        ("most valuable", "Most Valuable"),
        ("valuable", "Valuable"),
        ("high", "High"),
        ("moderate", "Moderate"),
        ("low", "Low"),
    ]

    title = models.CharField(max_length=100)
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES)
    description = models.TextField(blank=True)
    estimated_duration = models.DurationField(null=True, blank=True)
    deadline = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.deadline:
            now = timezone.now() if timezone.is_aware(self.deadline) else timezone.make_aware(datetime.now(), timezone.get_current_timezone())
            deadline = self.deadline if timezone.is_aware(self.deadline) else timezone.make_aware(self.deadline, timezone.get_current_timezone())
            duration = deadline - now
            self.estimated_duration = max(duration, timedelta(seconds=0))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
