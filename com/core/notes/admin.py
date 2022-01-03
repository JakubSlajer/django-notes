from django.contrib import admin
from .models import UserProfile, Note

admin.site.site_header = "Admin Tutorial Dashboard"

class SnippetAdmin(admin.ModelAdmin):
    exclude = 'title'


admin.site.register(UserProfile)
admin.site.register(Note)
