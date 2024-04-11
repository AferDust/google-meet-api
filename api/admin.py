from django.contrib import admin
from .models import Program, ProgramFAQ


class ProgramFAQInline(admin.TabularInline):
    model = ProgramFAQ
    extra = 1
    min_num = 1
    fields = ('question', 'answer', 'link')


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'link')
    inlines = [ProgramFAQInline]


@admin.register(ProgramFAQ)
class ProgramFAQAdmin(admin.ModelAdmin):
    list_display = ('program', 'question', 'answer', 'link')
    list_filter = ('program',)
    search_fields = ('question', 'answer')
