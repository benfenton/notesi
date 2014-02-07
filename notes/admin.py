from django.contrib import admin

from notes.models import Note


class NoteAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'title', 'text', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('title', 'text')

    fieldsets = [
        ('Note', {
            'fields': ('title', 'text')
          })
    ]
    readonly_fields = ('created_at', 'updated_at')

admin.site.register(Note, NoteAdmin)


