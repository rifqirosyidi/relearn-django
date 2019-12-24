from django.contrib import admin
from .models import Tutorial, TutorialSeries, TutorialCategory
from tinymce import TinyMCE
from django.db import models


# Register your models here.
class TutorialAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Title/Content', {'fields': ['tutorial_title', 'tutorial_content']}),
        ('URL', {'fields': ['tutorial_slug']}),
        ('Series', {'fields': ['tutorial_series']}),
        ('Date Published', {'fields': ['tutorial_publish']})
    ]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }


admin.site.register(TutorialCategory)
admin.site.register(TutorialSeries)
admin.site.register(Tutorial, TutorialAdmin)

