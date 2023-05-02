from django.contrib import admin
from .models import product,category,Order
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

class OrderAdmin(admin.ModelAdmin):
    list_display=('user','address','order_details','total_price','payment_mode','is_paid','is_delivered','created_at','deleted_at')
    ordering=('created_at',)
    list_editable=('is_delivered','is_paid',)
    search_fields=('name',)
    list_filter=('is_paid','is_delivered','payment_mode',)

admin.site.register(category,CategoryAdmin)
admin.site.register(product,ProductAdmin)
admin.site.register(Order,OrderAdmin)
