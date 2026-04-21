from django.contrib import admin
from .models import Contact, MessageUser, Subscription, Banner

# Register your models here.

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'city', 'country', 'email1')
    
    
@admin.register(MessageUser)
class MessageUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'created_at', 'processed')
    list_filter = ('created_at', 'processed')
    search_fields = ('first_name', 'last_name', 'email', 'message')
    ordering = ('-created_at', )
    readonly_fields = ('created_at', 'processed')
    

@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'created_at')
    list_filter = ('email', )
    ordering = ('-created_at', )
    readonly_fields = ('created_at', )
    
@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'type', 'active')
    list_filter = ('type', 'active')
    search_fields = ('title', 'subtitle')
    ordering = ('-id', )
    list_editable = ('active', )