from django.contrib import admin

from clock.models import Clock


@admin.register(Clock)
class ClockAdmin(admin.ModelAdmin):
    ...
