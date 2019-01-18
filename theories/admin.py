from django.contrib import admin
from .models import Theory


class TheoryAdmin(admin.ModelAdmin):
    class Meta:
        verbose_name_plural = "Theories"

    list_display = ('id', 'title')
    list_display_links = ('id', 'title')


admin.site.register(Theory, TheoryAdmin)
