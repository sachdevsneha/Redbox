from django.contrib import admin
from .models import Product, Category


# Register your models here.
'''@admin.register(Movies)
class MoviesModelAdmin(admin.ModelAdmin):
    list_display = ['name','IMDB_rating']


@admin.register(Reviews)
class ReviewsModelAdmin(admin.ModelAdmin):
    list_dispßlay = ['name']'''


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price','category', 'created_at','updated_at')
    list_display_links = ('name',)
    list_per_page = 50
    ordering = ['-created_at']
    search_fields = ['name', 'description']
    exclude = ('created_at','updated_at')

admin.site.register(Product, ProductAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    list_per_page = 20
    ordering = ['name']
    search_fields = ['name', 'description']

admin.site.register(Category,CategoryAdmin)



