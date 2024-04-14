from django.contrib import admin
from .models import *


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


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'address', 'phone_number']
    search_fields = ['user__username', 'phone_number']

@admin.register(Bank)
class BankAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']
    list_filter = ['name']

@admin.register(BankCardType)
class BankCardTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'bank', 'url']
    list_filter = ['bank']
    search_fields = ['name', 'bank__name']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'category']
    search_fields = ['category']

@admin.register(Cashback)
class CashbackAdmin(admin.ModelAdmin):
    list_display = ['id', 'bank_card_type', 'percent', 'category', 'expired_date', 'has_qr_payment', 'has_card_payment']
    sortable_by = 'percent'
    list_filter = ['bank_card_type', 'category', 'expired_date']
    search_fields = ['bank_card_type__name', 'category__category']

@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ['id', 'number', 'user', 'card_type', 'expired_date']
    search_fields = ['number', 'user__username', 'card_type__name']
    list_filter = ['card_type', 'user']
