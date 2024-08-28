from django.contrib import admin
from website.models import Contact


class PostAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'published_date')
    search_fields = ['name', 'subject']
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_filter = ['subject', 'name']


admin.site.register(Contact, PostAdmin)
