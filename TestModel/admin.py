from django.contrib import admin

# Register your models here.
from django.contrib import admin
from TestModel.models import Test, Contact, Tag


# Register your models here.
class TagInline(admin.TabularInline):
    model = Tag


class ContactAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    inlines = [TagInline]  # Inline
    list_display = ('name', 'age', 'email')  # list
    fieldsets = (
        ['Main', {
            'fields': ('name', 'email'),
        }],
        ['Advance', {
            'classes': ('collapse',),  # CSS
            'fields': ('age',),
        }]
    )


admin.site.register(Contact, ContactAdmin)
admin.site.register([Test])
