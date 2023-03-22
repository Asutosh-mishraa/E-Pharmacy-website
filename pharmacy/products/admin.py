from django.contrib import admin
from .models import product,category
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display=(
        'category','created_at'
    )
    ordering=('category',)
class ProductAdmin(admin.ModelAdmin):
    list_display=('category','name','price','description','is_available',)
    ordering=('name',)
    list_editable=('is_available','price','description',)
    search_fields=('name',)
    list_filter=('is_available','price','category',)
admin.site.register(category,CategoryAdmin)
admin.site.register(product,ProductAdmin)