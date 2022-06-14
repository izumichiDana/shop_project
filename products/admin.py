from django.contrib import admin
from .models import *
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from django.utils.safestring import mark_safe

class ProductAdminForm(forms.ModelForm):
    description = forms.CharField(label='Описание', widget=CKEditorUploadingWidget())

    class Meta:
        model = Product
        fields = '__all__'

class ImageInline(admin.TabularInline):
    model = Image
    max_num = 12
    min_num = 1

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    list_display_links = ('name', )
    search_fields = ('name', )
    prepopulated_fields = {'slug': ('name', )}

class CollectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    list_display_links = ('name', )
    search_fields = ('name', )
    prepopulated_fields = {'slug': ('name', )}

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug','created_at', )
    inlines = [ImageInline,]
    form = ProductAdminForm
    prepopulated_fields = {'slug': ('name', )}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Collections, CollectionAdmin)



