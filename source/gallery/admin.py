from django.contrib import admin

from gallery.models import Photography


# Register your models here.
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'photo', 'created_at')
    list_filter = ('id', 'description', 'photo', 'created_at')
    search_fields = ('description', 'id')
    readonly_fields = ('id', 'created_at', 'updated_at',)

admin.site.register(Photography, PhotoAdmin)
