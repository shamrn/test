from django.contrib import admin
from .models import LeadState,Lead

@admin.register(LeadState)
class _(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Lead)
class _(admin.ModelAdmin):
    list_display = ('name',)