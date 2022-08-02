from django.contrib import admin
from .models import App, Card, Web, Teammate

@admin.register(App)
class AppAdmin(admin.ModelAdmin):
    list_display = ("product_name", "product_category", "product_picture", "product_client", "product_date", "product_url")

@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ("product_name", "product_category", "product_picture", "product_client", "product_date", "product_url")

@admin.register(Web)
class WebAdmin(admin.ModelAdmin):
    list_display = ("product_name", "product_category", "product_picture", "product_client", "product_date", "product_url")

@admin.register(Teammate)
class TeammateAdmin(admin.ModelAdmin):
    list_display = ("teammate_name", "teammate_photo", "teammate_job", "teammate_twitter", "teammate_facebook", "teammate_instagram", "teammate_linkedln")

# Register your models here.
