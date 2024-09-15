from django.contrib import admin
from .models import Post
from import_export.admin import ImportExportModelAdmin

class PostAdmin(ImportExportModelAdmin):
    list_display = [field.name for field in Post._meta.fields]

admin.site.register(Post,PostAdmin)

