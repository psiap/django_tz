from django.contrib import admin
from .models import Client, DealsFile
# Register your models here.

class ClientAdmin(admin.ModelAdmin):
    list_display = ('username','spent_money','gems')
    list_display_links = ('username','spent_money','gems')
    search_fields = ('username','spent_money','gems')

class DealsFileAdmin(admin.ModelAdmin):
    list_display = ('customer', 'item', 'total', 'quantity', 'date')
    list_display_links = ('customer', 'item', 'total', 'quantity', 'date')
    search_fields = ('customer', 'item', 'total', 'quantity', 'date')



admin.site.register(Client,ClientAdmin)
admin.site.register(DealsFile,DealsFileAdmin)