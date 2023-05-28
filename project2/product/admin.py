from django.contrib import admin
from django.utils.safestring import mark_safe
# Register your models here.
from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin
from product.models import Category,Product,Images

class ProductImageInline(admin.TabularInline):
    model = Images
    extra = 3


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title','status']
    readonly_fields = ('image_tag',)
    list_filter = ['status']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'price', 'amount', 'image_tag','status']
    readonly_fields = ('image_tag',)
    list_filter = ['status','category']
    inlines = [ProductImageInline]

class ImagesAdmin(admin.ModelAdmin):
    list_display = ['title','product','image','image_tag']
    readonly_fields = ('image_tag',)

class CategoryAdmin2(DraggableMPTTAdmin):
    mptt_indent_field = "title"
    list_display = ('tree_actions', 'indented_title',
                    'related_products_count', 'related_products_cumulative_count')
    list_display_links = ('indented_title',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        # Add cumulative product count
        qs = Category.objects.add_related_count(
                qs,
                Product,
                'category',
                'products_cumulative_count',
                cumulative=True)

        # Add non cumulative product count
        qs = Category.objects.add_related_count(qs,
                 Product,
                 'category',
                 'products_count',
                 cumulative=False)
        return qs

    def related_products_count(self, instance):
        return instance.products_count
    related_products_count.short_description = 'Bu Kategoriye Ait Listelenen Ürünler'

    def related_products_cumulative_count(self, instance):
        return instance.products_cumulative_count
    related_products_cumulative_count.short_description = 'İlgili Ürünlerin Sayısı'


admin.site.register(Category,CategoryAdmin2)
admin.site.register(Product,ProductAdmin)
admin.site.register(Images,ImagesAdmin)