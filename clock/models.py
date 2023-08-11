from django.db import models
from django.contrib.auth.models import User


class Clock(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    employee = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    entry_date = models.DateTimeField()
    out_date = models.DateTimeField()
    description = models.TextField()
    to_correction = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Clock"
        verbose_name_plural = "Clocks"

    def __str__(self) -> str:
        return f'{self.employee} - {self.entry_date} - {self.out_date} - {self.to_correction}'
